from local_bigquery.models import QueryParameter, QueryParameterValue
from local_bigquery.transform import query_params_to_duckdb


def test_query_params_to_duckdb():
    scalar_param = QueryParameter(
        parameterValue=QueryParameterValue(value="scalar_value")
    )
    struct_param = QueryParameter(
        name="user",
        parameterValue=QueryParameterValue(
            structValues={
                "id": QueryParameterValue(value="123"),
                "name": QueryParameterValue(value="John Doe"),
                "scores": QueryParameterValue(
                    arrayValues=[
                        QueryParameterValue(value="85"),
                        QueryParameterValue(value="90"),
                    ]
                ),
            }
        ),
    )
    params = [scalar_param, struct_param]
    duckdb_params = query_params_to_duckdb(params)
    assert duckdb_params == {
        "param0": "scalar_value",
        "user": {"id": "123", "name": "John Doe", "scores": ["85", "90"]},
    }

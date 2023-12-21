from .import_rdb import hello_prefect
from prefect_aws import S3Bucket

if __name__ == "__main__":
    hello_prefect.from_source(
        source=S3Bucket.load("aws-flows"),
        entrypoint="prefect-work/hello_prefect/import_rdb.py:hello_prefect"
    ).deploy(
        name="hello_prefect",
        work_pool_name="managed-execution"
    )
from typing import List, Dict
from helpers import (
    list_buckets,
    describe_instances,
    get_ec2_client,
    get_s3_client,
)


def print_bucket_names(s3_client) -> None:
    """
    Retrieve and print all S3 bucket names for the given client.

    Args:
        s3_client: A boto3 S3 client used to interact with AWS S3.
    """
    # Fetch list of bucket names from AWS S3
    bucket_names: List[str] = list_buckets(s3_client)

    # Print each bucket name
    for bucket_name in bucket_names:
        print(bucket_name)


def print_instance_ids(ec2_client) -> None:
    """
    Retrieve and print all EC2 instance IDs for the given client.

    Args:
        ec2_client: A boto3 EC2 client used to interact with AWS EC2.
    """
    # Get list of instance descriptions from AWS EC2
    instances: List[Dict[str, str]] = describe_instances(ec2_client)

    # Extract instance IDs into a separate list
    instance_ids: List[str] = []
    for instance in instances:
        instance_ids.append(instance["InstanceId"])

    # Print each instance ID
    for instance_id in instance_ids:
        print(instance_id)


if __name__ == "__main__":
    # Initialize AWS EC2 and S3 clients
    ec2_client = get_ec2_client()
    s3_client = get_s3_client()

    # Print bucket names
    print_bucket_names(s3_client)

    # Print instance IDs
    print_instance_ids(ec2_client)

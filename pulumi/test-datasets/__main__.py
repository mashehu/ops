"""An AWS Python Pulumi program"""

import pulumi
import pulumi_aws as aws

awsmegatests_bucket = aws.s3.Bucket(
    "test-datasets-bucket",
    arn="arn:aws:s3:::nf-core-test-datasets",
    bucket="nf-core-test-datasets",
    cors_rules=[
        aws.s3.BucketCorsRuleArgs(
            allowed_headers=["*"],
            allowed_methods=[
                "HEAD",
                "GET",
            ],
            allowed_origins=[
                "https://s3.amazonaws.com",
                "https://s3-eu-west-1.amazonaws.com",
                "https://s3.eu-west-1.amazonaws.com",
                "*",
            ],
            expose_headers=[
                "ETag",
                "x-amz-meta-custom-header",
            ],
            max_age_seconds=0,
        )
    ],
    lifecycle_rules=[
        aws.s3.BucketLifecycleRuleArgs(
            abort_incomplete_multipart_upload_days=0,
            enabled=True,
            expiration=aws.s3.BucketLifecycleRuleExpirationArgs(
                date="",
                days=10,
                expired_object_delete_marker=False,
            ),
            id="Delete_files_older_than_10_days_in_work_directory",
            noncurrent_version_transitions=[],
            prefix="work",
            tags={},
            transitions=[],
        ),
        aws.s3.BucketLifecycleRuleArgs(
            abort_incomplete_multipart_upload_days=0,
            enabled=True,
            expiration=aws.s3.BucketLifecycleRuleExpirationArgs(
                date="",
                days=10,
                expired_object_delete_marker=False,
            ),
            id="Delete files older than 10 days in _nextflow folder",
            noncurrent_version_transitions=[],
            prefix="_nextflow",
            tags={},
            transitions=[],
        ),
        aws.s3.BucketLifecycleRuleArgs(
            abort_incomplete_multipart_upload_days=0,
            enabled=True,
            expiration=aws.s3.BucketLifecycleRuleExpirationArgs(
                date="",
                days=10,
                expired_object_delete_marker=False,
            ),
            id="Delete files older than 10 days in scratch directory",
            noncurrent_version_expiration=aws.s3.BucketLifecycleRuleNoncurrentVersionExpirationArgs(
                days=1,
            ),
            noncurrent_version_transitions=[],
            prefix="scratch",
            tags={},
            transitions=[],
        ),
        aws.s3.BucketLifecycleRuleArgs(
            abort_incomplete_multipart_upload_days=0,
            enabled=True,
            id="Move_to_intelligent_tier_after_11_days",
            noncurrent_version_transitions=[],
            prefix="",
            tags={},
            transitions=[
                aws.s3.BucketLifecycleRuleTransitionArgs(
                    date="",
                    days=11,
                    storage_class="INTELLIGENT_TIERING",
                )
            ],
        ),
    ],
    request_payer="BucketOwner",
    server_side_encryption_configuration=aws.s3.BucketServerSideEncryptionConfigurationArgs(
        rule=aws.s3.BucketServerSideEncryptionConfigurationRuleArgs(
            apply_server_side_encryption_by_default=aws.s3.BucketServerSideEncryptionConfigurationRuleApplyServerSideEncryptionByDefaultArgs(
                sse_algorithm="AES256",
            ),
        ),
    ),
)

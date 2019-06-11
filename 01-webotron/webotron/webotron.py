#!/usr/bin/python
# -*- coding: utf-8 -*-

"""Webotron: Automatically sync S3 buckets.

Webotron automates the process of syncing S3 buckets.
- Create AWS S3 Bucket
- Configure and set it up
- Sync local files
"""

import boto3
import click

from bucket import BucketManager

session = boto3.Session(profile_name='alexa-info-isengard')
bucket_manager = BucketManager(session)


@click.group()
def cli():
    """Webotron syncs files to S3."""
    pass


@cli.command('list-buckets')
def list_buckets():
    """List all s3 buckets."""
    for bucket in bucket_manager.all_buckets():
        print(bucket)


@cli.command('list-bucket-objects')
@click.argument('bucket')
def list_bucket_objects(bucket):
    """List objects in an S3 bucket."""
    for obj in bucket_manager.all_objects(bucket):
        print(obj)


@cli.command('setup-bucket')
@click.argument('bucket')
def setup_bucket(bucket):
    """Create and configure S3 bucket."""
    s3_bucket = bucket_manager.init_bucket(bucket)
    bucket_manager.set_policy(s3_bucket)


@cli.command('sync')
@click.argument('pathname', type=click.Path(exists=True))
@click.argument('bucket')
def sync(pathname, bucket):
    """Sync contents of pathname to bucket."""
    bucket_manager.sync_bucket(pathname, bucket)


if __name__ == '__main__':
    cli()

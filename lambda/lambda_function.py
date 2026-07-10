def lambda_handler(event, context):

    for record in event["Records"]:

        bucket = record["s3"]["bucket"]["name"]
        file = record["s3"]["object"]["key"]

        print("Bucket :", bucket)
        print("File :", file)

    return {
        "statusCode":200
    }
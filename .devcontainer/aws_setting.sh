AWS_ACCESS_KEY_ID=`jq -r ".aws.aws_access_key_id" "/config.json"`
AWS_SECRET_ACCESS_KEY=`jq -r ".aws.aws_secret_access_key" "/config.json"`
REGION_NAME=`jq -r ".aws.region_name" "/config.json"`

aws configure set aws_access_key_id $AWS_ACCESS_KEY_ID
aws configure set aws_secret_access_key $AWS_SECRET_ACCESS_KEY
aws configure set default.region $REGION_NAME
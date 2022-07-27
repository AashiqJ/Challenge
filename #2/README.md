## Challenge #2

We need to write code that will query the meta data of an instance within AWS and provide a
json formatted output. The choice of language and implementation is up to you.
Bonus Points
The code allows for a particular data key to be retrieved individually

## Solution

*Prerequisites*
 * Boto3, you can install boto3 from PyPI with:
    ``` 
    python -m pip install boto3
    ```
 * set up credentials (in e.g. ~/.aws/credentials):
    ```
    [default]
    aws_access_key_id = YOUR_KEY
    aws_secret_access_key = YOUR_SECRET
    ```

Run the program using ``` python app.py ```. The application will ask for the instance-id. Once the instance-id is given as input you will get an json output will all the details of the instance.

Additionally, you will get another user input option with options on any specific value to print.
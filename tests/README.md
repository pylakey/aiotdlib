# aiotdlib Tests

## Running the tests

### Setup

To run the tests, you must set the following environment variables in your test environment

| Environment Variable  | Note                                                             |
|-----------------------|------------------------------------------------------------------|
| AIOTDLIB_API_ID       | Your API ID from <https://my.telegram.org/apps>                  |
| AIOTDLIB_API_HASH     | Your API Hash from <https://my.telegram.org/apps>                |
| AIOTDLIB_PHONE_NUMBER | Phone number in international format registered in production DC |

In PyCharm, you can do this by creating a `pytest` Run/Debug configuration with
a `script` target of `/path/to/aiotdlib/tests`, working directory of `/path/to/aiotdlib/tests`
and Environment Variables of the above variables separated by semicolons.

### Test execution

When running the tests that require a real account, you can't get around receiving
an MFA code from Telegram. To support this, the login process will read a code from 
the file `tests/code.txt`. When launching the tests, make sure you're logged in to
the same account from another Telegram app. Once you receive the MFA code from Telegram,
copy and paste it into `tests/code.txt` and save the file. Don't worry about extra
spaces / newlines. The test process will pick up the code and then overwrite the file
so it's empty for next time.

For non-login tests, the default storage directory will be used, and it will _not_
be wiped in between tests - therefore, after the first login you should not need
to repeat the login process again.

### Account requirements

Currently, the tests only require that your account is a member of at least one chat.

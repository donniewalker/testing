How to retain the same session ID of a previous webdriver instance to get around multi-factor authentication

Before executing tests run following command in terminal (mac):

/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222 --no-first-run --no-default-browser-check --user-data-dir=$(mktemp -d -t 'chrome-remote_data_dir')



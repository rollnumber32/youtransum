# youtransum

**Technologies used:** Chrome extension tools, Flask

YouTube transcript summarizer.

## Follow these steps to run locally

1. Open terminal and clone repository

```
git clone git@github.com:rollnumber32/youtransum.git
```

2. Open backend server directory

```
cd youtransum/backend
```

3. Create virtual environment.

```
python3 -m venv .venv
```

4. Install all the required dependencies

```
pip install -r requirements.txt
```

5. Run flask server

```
python app.py
```

6. Go to chrome and open given link

```
chrome://extensions
```

7. Turn on developer mode from top right
8. Load extension by clicking option on top left

...and you are good to go.

**Note**: You'll need to install the (this)[https://chrome.google.com/webstore/detail/allow-cors-access-control/lhobafahddgcelffkeicbaginigeejlf?hl=en] chrome extension too.
**Note**: You must have python and pip installed.

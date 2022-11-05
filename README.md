# DuckDuckGo API Test

The purpose of this test is to identify if `presidents of the united states` search returns the 45 names of the US presidents. 

Run to have all the modules needed 
```
pip install -r requirements.txt
```

We have 4 test cases 

- `test_ddg_appear_names_presidents` loops though the us_presidents list to check if all the presidents appear in the response. 
- `test_all_presidents_true` uses president_dic where it creates a dictionary with the name as a key and True/False as a value to identify if the president is in the response. Then, the test checks if all the values in the dictionary are True, the test is successful. 
- `test_45_presidents` checks if the dictionary has 45 keys which represent the 45 presidents of the United States. 
- `test_successful_call` checks if the status code is 200 which represents a successful call. 

Run 
```
pytest test_duckduckgo.py
```

### Documentation 

https://help.duckduckgo.com/duckduckgo-help-pages/results/syntax/

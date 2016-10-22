# TEST FOR COGNIANCE

## PYTHON

Platform Windows10, python-2.7.12,  pip-8.1.2, requests-2.11.1

### STEPS

  Install Python-2.7.12. You can download it here https://www.python.org/downloads/release/python-2712/.
  
  
  Add Python to path: System -> Advanced system settings ->Environment Variables… ->Edit variable with the name Path.
  
  
  Install request module for Python-2.7.12 with cmd. Yoг can download it here https://pypi.python.org/pypi/requests/2.11.1
  ```sh
  $ python -m pip install -U pip
  $ python -m pip install requests
  ```
  Download QAinterviewCogniance.py here "ccилка на мый репозиторій"
  
  
  Go to directory where is "QAinterviewCogniance.py". Run with cmd.
  ```sh
  $ python QainterviewCogniance.py
  ```
## DATAMINING

  Download access log :http://qainterview.cogniance.com/datamining.log
   
   
  Count # of successful requests per hour and store results in file "results.txt" with Linux cmd
  ```sh
   $ grep -o '200' datamining.log | wc -l > 'results.txt'
  ``` 
 
   
	

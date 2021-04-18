# pytest-selenium

[pytest]: https://docs.pytest.org/en/6.2.x/index.html
[Selenium]: https://www.selenium.dev
[OpenMRS]: https://openmrs.org
[Demo site]: https://demo.openmrs.org/openmrs/login.htm
[Docker]: https://wiki.openmrs.org/display/docs/Installing+OpenMRS+on+Docker
[docker-compose]: docker-compose.yml
[pytest]/[Selenium] framework for testing [OpenMRS] ([Demo site] or [Docker] via [docker-compose])

## requirements
* [Python](https://www.python.org/downloads/) (tested on version 3.9.2)
* Web browser ([Google Chrome](https://google.com/chrome) is used by default)

## how to run
1. Install required libraries:</br>
`python -m pip install -r requirements.txt`

2. Run the test suite:</br>
`python -m pytest .\tests\`

## configuration
[test_variables.toml](/utils/test_variables.toml):
* `[test]url_local` -> local hosted AUT address
* `[test]url` -> remote hosted AUT address
* `[driver]default` -> web browser to run tests on (e.g. `chrome`, `firefox`)
* `[driver]wait` -> Default wait/timeout

## main features:
* browser selection using command line parameter `--browser`
* using `url_local` if HTTP response == 200 or `url` if HTTP response of `url_local` <> 200
* test logs/reports/error screenshots stored in the `output` folder
* test data stored in `output/testdata_yyyyMMdd.xlsx`

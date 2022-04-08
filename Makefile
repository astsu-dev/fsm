fmt:
	isort fsm tests docs_src
	black fsm tests docs_src
test:
	pytest -vvv tests

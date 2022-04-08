fmt:
	isort fsm tests
	black fsm tests
test:
	pytest -vvv tests

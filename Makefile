.PHONY: run
run: venv rendezvous.py
	./venv/bin/python3 rendezvous.py

.PHONY: typecheck
typecheck: venv rendezvous.py
	./venv/bin/mypy rendezvous.py

venv: requirements.txt
	python3 -m venv venv
	./$@/bin/python3 -m pip install --upgrade pip setuptools wheel
	./$@/bin/python3 -m pip install -r $<


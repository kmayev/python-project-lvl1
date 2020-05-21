cd ~/Documents/tests
rm -r test_env
asciinema rec
python3 -m venv test_env
test_env/bin/pip install --upgrade pip
test_env/bin/pip install  -i https://test.pypi.org/simple/ kmayev-brain-games --extra-index-url https://pypi.org/simple/ --no-cache-dir 
test_env/bin/brain-gcd

from flask import Flask
from argparse import ArgumentParser

from blockchain import BlockChain
from interface import User

app = Flask(__name__)

if __name__ == "__main__":
    parser = ArgumentParser()
    parser.add_argument('-H', '--host', default='127.0.0.1')
    parser.add_argument('-p', '--port', default=8000, type=int)
    parser.add_argument('-pass', '--password', required=True)
    args = parser.parse_args()
    
    user = User(args.password, args.host, args.port)
    blockchain = BlockChain()

    app.run(debug=True, host=args.host, port=args.port)
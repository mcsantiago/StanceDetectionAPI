#!/usr/bin/env python3

import connexion

from swagger_server import encoder


def main():
    app = connexion.App(__name__, specification_dir='./swagger/')
    app.app.json_encoder = encoder.JSONEncoder
    app.add_api('swagger.yaml', arguments={
                'title': 'Topic Stance Detector API'}, pythonic_params=True)
    app.run(host='127.0.0.1', port=8080)


if __name__ == '__main__':
    main()

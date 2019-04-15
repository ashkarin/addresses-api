from flask import request, send_file
from flask_restplus import Resource, Namespace

api = Namespace('address', description='address related operations')


@api.route('/')
class AddressDistribution(Resource):
    @api.doc('get distribution of addresses by zip code')
    def get(self):
        return "root", 200


@api.route('/img')
class AddressDistributionImage(Resource):
    @api.doc('get image of distribution of addresses by zip code')
    def get(self):
        return "/img", 200


@api.route('/<zip_code>')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class AddressDistributionByZipcode(Resource):
    @api.doc('get number of addresses for a zip code')
    def get(self, zip_code):
        return "/%s" % zip_code, 200


@api.route('/<zip_code>/img')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class AddressDistributionByZipcodeImage(Resource):
    @api.doc('get number of addresses for a zip code')
    def get(self, zip_code):
        return "/%s/img" % zip_code, 200


@api.route('/years')
class YearsDistribution(Resource):
    @api.doc('get distribution of addresses by years')
    def get(self):
        return "years", 200


@api.route('/years/img')
class YearsDistributionImage(Resource):
    @api.doc('get image of distribution of addresses by years')
    def get(self):
        return "years/img", 200


@api.route('/years/<zip_code>')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class YearsDistributionByZipcode(Resource):
    @api.doc('get distribution of addresses with a zip code by years')
    def get(self, zip_code):
        return "years/%s" % zip_code, 200


@api.route('/years/<zip_code>/img')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class YearsDistributionByZipcodeImage(Resource):
    @api.doc('get distribution of addresses with a zip code by years')
    def get(self, zip_code):
        return "years/%s/img" % zip_code, 200

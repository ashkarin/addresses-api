from flask import request, send_file
from flask_restplus import Resource, Namespace

from myapp.db import get_dist_builings_by_years, get_dist_builings_by_zip
from myapp.utils import plot_barchart, generate_random_name


api = Namespace('address', description='address related operations')


@api.route('/')
class AddressDistribution(Resource):
    @api.doc('get distribution of addresses by zip code')
    def get(self):
        dist = get_dist_builings_by_zip()
        if not dist:
            return {'status': 'error', 'data': 'No data available'}, 400
        else:
            return {'status': 'success', 'data': dist}, 200


@api.route('/img')
class AddressDistributionImage(Resource):
    @api.doc('get image of distribution of addresses by zip code')
    def get(self):
        dist = get_dist_builings_by_zip()
        if not dist:
            api.abort(404)
        else:
            buf = plot_barchart(dist,
                                threshold=0,
                                title='Address distribution by zip codes',
                                y_label='Number of addresses')
            name = generate_random_name()
            return send_file(buf, attachment_filename=name + '.jpeg', mimetype='image/jpg')


@api.route('/<zip_code>')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class AddressDistributionByZipcode(Resource):
    @api.doc('get number of addresses for a zip code')
    def get(self, zip_code):
        dist = get_dist_builings_by_zip(zip_code=zip_code)
        if not dist:
            api.abort(404)
        else:
            return {'status': 'success', 'data': dist}, 200


@api.route('/<zip_code>/img')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class AddressDistributionByZipcodeImage(Resource):
    @api.doc('get number of addresses for a zip code')
    def get(self, zip_code):
        dist = get_dist_builings_by_zip(zip_code=zip_code)
        if not dist:
            api.abort(404)
        else:
            buf = plot_barchart(dist,
                                threshold=0,
                                title='Address distribution for a zip code ({})'.format(zip_code),
                                y_label='Number of addresses')
            name = generate_random_name()
            return send_file(buf, attachment_filename=name + '.jpeg', mimetype='image/jpg')


@api.route('/years')
class YearsDistribution(Resource):
    @api.doc('get distribution of addresses by years')
    def get(self):
        dist = get_dist_builings_by_years()
        if not dist:
            api.abort(404)
        else:
            return {'status': 'success', 'data': dist}, 200


@api.route('/years/img')
class YearsDistributionImage(Resource):
    @api.doc('get image of distribution of addresses by years')
    def get(self):
        dist = get_dist_builings_by_years()
        if not dist:
            api.abort(404)
        else:
            buf = plot_barchart(dist,
                                threshold=0,
                                title='Address distribution by years',
                                y_label='Number of addresses')
            name = generate_random_name()
            return send_file(buf, attachment_filename=name + '.jpeg', mimetype='image/jpg')


@api.route('/years/<zip_code>')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class YearsDistributionByZipcode(Resource):
    @api.doc('get distribution of addresses with a zip code by years')
    def get(self, zip_code):
        dist = get_dist_builings_by_years(zip_code=zip_code)
        if not dist:
            api.abort(404)
        else:
            return {'status': 'success', 'data': dist}, 200


@api.route('/years/<zip_code>/img')
@api.param('zip_code', 'The zip code of address')
@api.response(404, 'Zip code is not found.')
class YearsDistributionByZipcodeImage(Resource):
    @api.doc('get distribution of addresses with a zip code by years')
    def get(self, zip_code):
        dist = get_dist_builings_by_years(zip_code=zip_code)
        if not dist:
            api.abort(404)
        else:
            buf = plot_barchart(dist,
                                threshold=0,
                                title='Address distribution by years for ({})'.format(zip_code),
                                y_label='Number of addresses')
            name = generate_random_name()
            return send_file(buf, attachment_filename=name + '.jpeg', mimetype='image/jpg')

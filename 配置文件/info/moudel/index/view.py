from . import index_blu


@index_blu.route('/index1')
def index1():
    return 'hallo world'

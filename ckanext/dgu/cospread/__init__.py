from ckanext.importlib.api_command import ApiCommand
from ckanext.dgu.command import XmlRpcCommand
from ckanext.dgu.cospread.cospread import CospreadImporter
from ckanext.dgu.cospread.loader import CospreadLoader
from ckanclient import CkanClient

class CospreadCommand(ApiCommand, XmlRpcCommand):
    usage = 'usage: %prog [options] {metadata.xls}'

    def add_options(self):
        super(CospreadCommand, self).add_options()
        self.parser.add_option("-t", "--include-given-tags",
                               dest="include_given_tags",
                               action="store_true",
                               default=False,
                               help="Uses source's tags (in addition to just common keywords found.)")

    def command(self):
        super(CospreadCommand, self).command()

        if len(self.args) != 1:
            self.parser.error('You must specify metadata file')
        else:
            data_filepath = self.args[0]
        importer = CospreadImporter(
            filepath=data_filepath,
            xmlrpc_settings=self.xmlrpc_settings,
            include_given_tags=self.options.include_given_tags,
            )
        
        loader = CospreadLoader(self.client)
        loader.load_packages(importer.pkg_dict())

def load():
    CospreadCommand().command()

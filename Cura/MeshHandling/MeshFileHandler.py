class MeshFileHandler(object):
    def __init__(self):
        self._mesh_readers = []
        self._mesh_writers = []
    
    # Try to read the mesh_data from a file. Based on the extension in the file a correct meshreader is selected.
    # \param file_name The name of the mesh to load.
    # \returns MeshData if it was able to read the file, None otherwise.
    def read(self, file_name):
        for reader in self._mesh_readers:
            result = reader.read(file_name) 
            if(result is not None):
                return result
        return None #unable to read
    
    # Try to write the mesh_data to file. Based on the extension in the file_name a correct meshwriter is selected.
    # \param file_name The name of the file to write.
    # \param mesh_data
    # \returns True if it was able to create the file, otherwise False
    def write(self, file_name, mesh_data):
        if(mesh_data is None):
            return False
        for writer in self._mesh_writers:
            if(writer.write(file_name, mesh_data)):
                return True
        return False
    
    # Get list of all supported filetypes for writing.
    # \returns List of strings with all supported filetypes.
    def getSupportedFileTypesWrite(self):
        supported_types = []
        for writer in self._mesh_writer:
            supported_types.append(writer.getSupportedExtension())
        return supported_types
    
    # Get list of all supported filetypes for reading.
    # \returns List of strings with all supported filetypes.
    def getSupportedFileTypesRead(self):
        supported_types = []
        for reader in self._mesh_readers:
            supported_types.append(reader.getSupportedExtension())
        return supported_types
        
    def addWriter(self, writer):
        self._mesh_writers.append(writer)
        
    def addReader(self, reader):
        self._mesh_readers.append(reader)
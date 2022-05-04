from ast import Str


class Cancion:
    def __init__(self, Titulo, Duracion, Reproducciones, Artista, CasaDisquera, Repeticiones, Album, CancionesExplicitas,Playlist):

        self.Titulo = Titulo(str)
        self.Duracion = Duracion(int)
        self.Reproducciones = Reproducciones(int)
        self.Artista = Artista
        self.CasaDisquera= CasaDisquera
        self.Repeticiones= Repeticiones(int)
        self.Album = Album
        self.CancionesExplicitas = CancionesExplicitas(bool)
        
        def GetTitulo (self):
            """Titulo de cancion."""
            input("ingrese titulo de la cancion")
            def SetDuracion (self):
                """Duracion."""
                print(f"Duracion, {self.Duracion}")
                def SetReproducciones (self):
                    """Reproducciones."""
                    print(f"Reproducciones, {self.Reproducciones}")
                    def SetArtista (self):
                        """Artista."""
                        input("ingrese artista")
                        def SetCasaDisquera (self):
                            """Casa disquera."""
                            print(f"Casa Disquera, {self.CasaDisquera}")
                            def SetRepeticiones (self):
                                """Repeticiones."""
                                print(f"Repeticiones, {self.Repeticiones}")
                                def GetCancionesExplicitas (self):
                                    """Canciones explicitas."""
                                    input("ingrese canciones explicitas")
                                    def SetAlbum (self):
                                        """album."""
                                        print(f"album, {self.album}")
        self.ObtenerArtista=self,artista=Artista,foto=str,bio=str,nombre=str
        self.ObtenerAlbum=self,album=Album,titulo=str,foto=str,año=str
        self.ObtenerTitulo=self,titulo=Titulo

                                        

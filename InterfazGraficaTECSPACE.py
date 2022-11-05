from tkinter import *

def pantallainicio():
    def pantallaproyectos():
        def botonatras():
            PantallaProyectos.destroy()
            pantallainicio()


        def proyectointroduccion():
            def botonatras1():
                PantallaProyectoIntroduccion.destroy()
                pantallaproyectos()


            def pantalladatos():
                def botonatras2():
                    PantallaDatosProyectoIntroduccion.destroy()
                    proyectointroduccion()

                def datosAceleracion():
                    def botonatras5():
                        PantallaVariable1Datos.destroy()
                        pantalladatos()

                    PantallaDatosProyectoIntroduccion.destroy()

                    PantallaVariable1Datos = Label(ventana, width=500, height=500,bg='#0B2C49', fg='white')
                    PantallaVariable1Datos.pack()
                    CuadroAceleracion = Label(PantallaVariable1Datos, text='Aceleración',font=('Times_New_Roman', 40),
                                              bg='#0B2C49', fg='white' )
                    CuadroAceleracion.place(x=120, y=10)

                    botonatras5 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras5)
                    botonatras5.place(x=7,y=7)

                def datosAltura():
                    def botonatras6():
                        PantallaVariable2Datos.destroy()
                        pantalladatos()

                    PantallaDatosProyectoIntroduccion.destroy()

                    PantallaVariable2Datos = Label(ventana,  width=500, height=500,bg='#0B2C49', fg='white')
                    PantallaVariable2Datos.pack()
                    CuadroAltura = Label(PantallaVariable2Datos, text='Altura',font=('Times_New_Roman', 40),
                                              bg='#0B2C49', fg='white' )
                    CuadroAltura.place(x=180, y=10)

                    botonatras6 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras6)
                    botonatras6.place(x=7,y=7)

                def datosTiempo():
                    def botonatras7():
                        PantallaVariable3Datos.destroy()
                        pantalladatos()

                    PantallaDatosProyectoIntroduccion.destroy()

                    PantallaVariable3Datos = Label(ventana,  width=500, height=500,bg='#0B2C49', fg='white')
                    PantallaVariable3Datos.pack()
                    CuadroTiempo = Label(PantallaVariable3Datos, text='Tiempo',font=('Times_New_Roman', 40),  bg='#0B2C49', fg='white')
                    CuadroTiempo.place(x=160, y=10)

                    botonatras7 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras7)
                    botonatras7.place(x=7,y=7)

                def datosGPS():
                    def botonatras8():
                        PantallaVariable4Datos.destroy()
                        pantalladatos()

                    PantallaDatosProyectoIntroduccion.destroy()

                    PantallaVariable4Datos = Label(ventana, width=500, height=500,bg='#0B2C49', fg='white')
                    PantallaVariable4Datos.pack()
                    CuadroGPS = Label(PantallaVariable4Datos, text='GPS',  font=('Times_New_Roman', 40),bg='#0B2C49', fg='white')
                    CuadroGPS.place(x=190, y=10)

                    botonatras8 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras8)
                    botonatras8.place(x=7,y=7)


                PantallaProyectoIntroduccion.destroy()

                PantallaDatosProyectoIntroduccion = Label(ventana, width=500, height=500, bg='#0B2C49')
                PantallaDatosProyectoIntroduccion.pack()

                CuadroDatosProyectoIntroduccion = Label(PantallaDatosProyectoIntroduccion,
                                                        text='Datos', font=('Times_New_Roman', 40), fg='white', bg='#0B2C49')
                CuadroDatosProyectoIntroduccion.place(x=180,y=10)

                botonatras2 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras2)
                botonatras2.place(x=7,y=7)

                boton_aceleracion = Button(PantallaDatosProyectoIntroduccion, text='Aceleración',
                                        font=('Times_New_Roman', 15), command=datosAceleracion, fg='#0B2C49')
                boton_aceleracion.place(x=100,y=100)

                boton_altura = Button(PantallaDatosProyectoIntroduccion, text='Altura',
                                        font=('Times_New_Roman', 15), command=datosAltura, fg='#0B2C49')
                boton_altura.place(x=300, y=100)

                boton_tiempo = Button(PantallaDatosProyectoIntroduccion, text='Tiempo',
                                        font=('Times_New_Roman', 15), command=datosTiempo, fg='#0B2C49')
                boton_tiempo.place(x=120, y=300)

                boton_gps = Button(PantallaDatosProyectoIntroduccion, text='GPS',
                                        font=('Times_New_Roman', 15), command=datosGPS, fg='#0B2C49')
                boton_gps.place(x=305, y=300)

            def pantallagaleria():
                def botonatras3():
                    PantallaGaleriaProyectoIntroduccion.destroy()
                    proyectointroduccion()

                PantallaProyectoIntroduccion.destroy()

                PantallaGaleriaProyectoIntroduccion = Label(ventana, width=500, height=500,bg='#0B2C49')
                PantallaGaleriaProyectoIntroduccion.pack()

                CuadroGaleriaProyectoIntroduccion = Label(PantallaGaleriaProyectoIntroduccion,
                                                        text='Galeria', font=('Times_New_Roman', 40), bg='#0B2C49', fg='white')
                CuadroGaleriaProyectoIntroduccion.place(x=170,y=10)

                botonatras3 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras3)
                botonatras3.place(x=7,y=7)




            def pantallacodigo():
                def botonatras4():
                    PantallaCodigoIntroduccion.destroy()
                    proyectointroduccion()

                PantallaProyectoIntroduccion.destroy()

                PantallaCodigoIntroduccion = Label(ventana, width=500, height=500, bg='#0B2C49')
                PantallaCodigoIntroduccion.pack()

                CuadroCodigoProyectoIntroduccion = Label(PantallaCodigoIntroduccion,
                                                        text='Código', font=('Times_New_Roman', 40), bg='#0B2C49', fg='white')
                CuadroCodigoProyectoIntroduccion.place(x=180,y=10)

                botonatras4 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras4)
                botonatras4.place(x=7,y=7)

            PantallaProyectos.destroy()
            botonatras.destroy()

            PantallaProyectoIntroduccion = Label(ventana, height=500, width=500, bg='#0B2C49')
            PantallaProyectoIntroduccion.pack()

            cuadroProyectoIntroduccion = Label(PantallaProyectoIntroduccion, text='Proyecto de Introducción'
                                                                                  '\n a TECSPACE',
                                               font=('Times_New_Roman', 25), bg='#0B2C49', fg='white')
            cuadroProyectoIntroduccion.place(x=100,y=10)



            botonatras1 = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras1)
            botonatras1.place(x=7,y=7)

            botonDatos = Button(PantallaProyectoIntroduccion, text='Datos', font=('Times_New_Roman', 25), fg='#0B2C49',
                                command=pantalladatos)
            botonDatos.place(x=100, y=150)

            botonGaleria = Button(PantallaProyectoIntroduccion, text='Galeria', font=('Times_New_Roman', 25),fg='#0B2C49',
                                command=pantallagaleria)
            botonGaleria.place(x=300, y=150)

            botonCodigo = Button(PantallaProyectoIntroduccion, text='Codigo', font=('Times_New_Roman', 25),fg='#0B2C49',
                                  command=pantallacodigo)
            botonCodigo.place(x=200, y=300)

        PantallaInicio.destroy()
        botoninicio.destroy()

        PantallaProyectos = Label(ventana, height=500, width=500, bg='#0B2C49')
        PantallaProyectos.pack()

        cuadroProyectos = Label(PantallaProyectos, text='Proyectos', font=('Times_New_Roman', 40), bg='#0B2C49', fg='white')
        cuadroProyectos.place(x=125, y=10)



        botonatras = Button(ventana, text='Atras', font=('Times_New_Roman', 12), bg='white', fg='#0B2C49', command=botonatras)
        botonatras.place(x=7,y=7)

        botonProyectoIntroduccion = Button(PantallaProyectos, text='Proyecto de Introduccion',font=('Times_New_Roman',15),
                                           bg='white', fg='#0B2C49',
                                           command=proyectointroduccion)
        botonProyectoIntroduccion.place(x=25, y=100)

    PantallaInicio = Label(ventana, height=500, width=500, bg='#0B2C49')
    PantallaInicio.pack()
    CuadroTecSpace = Label(PantallaInicio, text='TECSPACE', font=('Times_New_Roman', 60), fg='white', bg='#0B2C49')
    CuadroTecSpace.place(x=40,y=120)
    botoninicio = Button(ventana, text='Inicio', font=('Times_New_Roman', 40), fg='#0B2C49', bg='white', command=pantallaproyectos)
    botoninicio.place(x=175,y=300)



ventana = Tk()
ventana.maxsize(height=500, width=500)
ventana.minsize(height=250, width=250)
ventana.title('TECSPACE')


# cambio de path al cambiar computadora
#ventana.iconbitmap("E:\\TECSPACE\\fotos\\icono.ico")
ventana.iconbitmap("D:\\tecspaceproyecto\\imagenes\\icono.ico")

pantallainicio()

ventana.mainloop()
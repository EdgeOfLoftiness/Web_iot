const express = require('express')
const mysql = require('mysql')
const bodyparser = require('body-parser')

const app = express()

app.use(bodyparser.json())

const PUERTO = 3000

const conexion = mysql.createConnection(
    {
        host:'db4free.net',
        database:'apidb1',
        user:'hins12',
        password:'Starward12@'
    }
)

app.listen(PUERTO, () => {
    console.log(`Servidor compilado en el puerto ${PUERTO}`)
})

conexion.connect(error => {
    if(error) throw error
    console.log('Conexion establecida OK.')
})

app.get('/clientes', (req,res) =>{
    const query = 'SELECT * FROM iot_android.clientes;'

    conexion.query(query, (error, resultado) => {
        if(error) return console.error(error.message)

        const obj = {}
        if(resultado.length > 0){
            obj.lista = resultado
            res.json(obj)
        }else{
            res.json('No hay Clientes registrados.')
        }
    })
})
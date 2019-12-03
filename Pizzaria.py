import os  
from peewee import *
from flask import Flask, json, jsonify
from playhouse.shortcuts import model_to_dict

arq="/home/aluno/Pizzaria/bla.bd"
db=SqliteDatabase(arq)


class BaseModel(Model):
    class Meta():
        database = db

class Pizza (BaseModel):
    sabor = CharField()
    preco_base = CharField()
    e_personalizada = CharField()
    
class Bebida (BaseModel):
    tipo_bebida = CharField()
    preco = CharField()

class Fornada (BaseModel):
    num_pizzas = CharField()
    num_da_fornada = CharField()


class Endereco (BaseModel):
    cep = CharField()
    rua = CharField()
    num_casa = CharField()
    cidade = CharField()
    bairro = CharField()


class Cliente (BaseModel):
    nome = CharField()
    login = CharField()
    senha = CharField()
    telefone = CharField()
    endereco_cliente = ForeignKeyField(Endereco)


class Pedido (BaseModel):
    dia = CharField()
    hora = CharField()
    prioridade = CharField()
    cliente = ForeignKeyField(Cliente)
    fornada = ForeignKeyField(Fornada)

class Bebida_Pedida (BaseModel):
    quantidade = CharField()
    pedido = ForeignKeyField(Pedido)
    bebida = ForeignKeyField(Bebida)


class Ingrediente (BaseModel):
    nome = CharField()
    preco = CharField()
    pizzas = ManyToManyField(Pizza)

class Tamanho (BaseModel):
    nome = CharField()
    desconto = CharField()

class Pizza_Pedida (BaseModel):
    quantidade = CharField()
    pedido = ForeignKeyField(Pedido)
    tamanho = ForeignKeyField(Tamanho)
    pizza = ForeignKeyField(Pizza)



if __name__ == "__main__":
    db.connect()
    db.create_tables([Pizza, Bebida, Bebida_Pedida, Cliente, Pedido, Ingrediente, Ingrediente.pizzas.get_through_model(), Pizza_Pedida, Fornada, Tamanho, Endereco])


pizza1= Pizza.create(sabor= "portuguesa" , preco_base= "21.00 reais" , e_personalizada="nao")
bebida1= Bebida.create(tipo_bebida= "guarana" , preco= "4.00 reais")
endereco1= Endereco.create(cep= "89120000" , rua= "amapa" , num_casa= "44" , cidade= "timbó" , bairro= "estados")
cliente1= Cliente.create(nome= "Matheus" , login= "matheus123" , senha= "123" , telefone= "1234-5667" , endereco_cliente= endereco1)
fornada1= Fornada.create(num_pizzas= "1" , num_da_fornada= "3" )
pedido1= Pedido.create(dia= "quarta" , hora= "14:00 horas" , prioridade= "alta" , cliente= cliente1 , fornada= fornada1)
bebida_pedida1= Bebida_Pedida.create(quantidade= "2" , pedido= pedido1 , bebida= bebida1)
tamanho1= Tamanho.create(nome= "media" , desconto= "5.00 reais")
pizza_pedida1= Pizza_Pedida.create(quantidade= "1" , pedido= pedido1 , tamanho= tamanho1 , pizza= pizza1)
ingrediente1= Ingrediente.create(nome= "queijo, presunto, cebola, azeitona, ovo" , preco= "10.00 reais")
ingrediente1.pizzas.add(pizza1)

print (pizza1.preco_base)



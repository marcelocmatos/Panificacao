from Fermento import Fermento

class Tipo_Fermento(object):
    
    def __init__(tipo_fermento, peso_fermento):
        self.tipo_fermento = int(tipo_fermento)
        self.peso_fermento = int(peso_fermento)
    
    def tipo_fermento(tipo_fermento, peso_fermento):
        tipo_fermento = tipo_fermento

        if tipo_fermento == 1:
          
            fermento123 = Fermento.fermento123(peso_fermento)
            return fermento123

        else:
            fermento122 = Fermento.fermento122(peso_fermento)
            return fermento122

   


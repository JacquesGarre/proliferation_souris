#! usr/bin/env python
# coding: utf-8


# Inspiré de https://trouwarat.forumgratuit.org/t191-afrma-folie-de-la-multiplication-des-souris


# Enoncé : 

# À quelle vitesse les souris se multiplient-elles ? 
# Commençons avec deux souriceaux, un de chaque sexe. 
# À l'âge de 6 semaines, la femelle peut être gestante. 
# La gestation dure 3 semaines, et en des conditions optimales la femelle peut être à nouveau gestante immédiatement après la mise à bas. 
# Prenons une portée de 8 souriceaux, 4 mâles et 4 femelles, qui sont mis en couple et reproduits dès leurs 6 semaines.

# - Combien aurais-je de souris en un an ?
# - Au bout de combien de temps aurais-je 500 souris?



class Souris:

  PORTEE_COUNT = 8 # capable de faire des portées de 8
  AGE_MINIMUM_REPRODUCTION = 42 # Elles sont capable de mettre bas à partir de l'âge de 6 semaines
  PORTEE = 1 # capable de faire des portées une fois par : 
  DUREE = 21 # La gestation dure 3 semaines

  def __init__(self, sexe):
    self.age = 0 # l'age de la souris en jours
    self.sexe = sexe

  def aging_process(self):
    self.age += 1

  @property
  def total_portees(self):
    if self.age >= self.AGE_MINIMUM_REPRODUCTION:
      portees_count = self.PORTEE * ((self.age - self.AGE_MINIMUM_REPRODUCTION)//self.DUREE)
    else:
      portees_count = 0
    return portees_count

  @property
  def total_children(self):
    return self.total_portees * self.PORTEE_COUNT

  @property
  def can_give_birth(self):
    # peut donner naissance si c'est une femelle, si l'age est supérieur à (AGE_MINIMUM_REPRODUCTION + durée de gestation) et si elle n'est pas gestante.
    return (self.sexe == 'femelle' and self.age >= (self.AGE_MINIMUM_REPRODUCTION + self.DUREE) 
            and (self.age - self.AGE_MINIMUM_REPRODUCTION + self.DUREE) % self.DUREE == 0)



class Elevage:

  def __init__(self, souris_initial_count):
    self.souris = []
    if(isinstance(souris_initial_count, int)):
      i = 0
      while i < souris_initial_count/2:
        self.add_souris(Souris('male'))
        i += 1
      while i < souris_initial_count:
        self.add_souris(Souris('femelle'))
        i += 1

  def generate_new_portee(self, souris_mere):
      i = 0
      while i < souris_mere.PORTEE_COUNT/2:
        self.add_souris(Souris('male'))
        i += 1
      while i < souris_mere.PORTEE_COUNT:
        self.add_souris(Souris('femelle'))
        i += 1

  def souris_count(self):
    return len(self.souris)

  def add_souris(self, souris):
    self.souris.append(souris)

  def nb_jours_pour_nb_souris(self, count): # retourne la durée nécessaire (en jours) pour obtenir "count" souris.
    t = 0
    while self.souris_count() <= count:
      for souris in self.souris:
        if souris.can_give_birth:
          self.generate_new_portee(souris)
        souris.aging_process()
      t += 1  
    return t

  def nb_souris_pour_nb_jours(self, count): # retourne le nombre de souris obtenues en "count" jours.
    n = self.souris_count()
    t = 0
    while t <= count:
      for souris in self.souris:
        if souris.can_give_birth:
          self.generate_new_portee(souris)
          n += Souris.PORTEE_COUNT
        souris.aging_process()
      t += 1  
    return n




def main():

  elevage = Elevage(2) # 2 étant le nombre initial de souris que je possède

  for i in range(1, 52):
    temps = 7 * i
    nb_souris = elevage.nb_souris_pour_nb_jours(temps)
    print("J'aurais {} souris au bout de {} semaines.".format(nb_souris, temps//7))
    print("--------------------------------------------")

if __name__=='__main__':
    main()  

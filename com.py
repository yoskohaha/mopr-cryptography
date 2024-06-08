class Mediator:
  def __init__(self):
      self.parties = {}

  def register(self, name, party):
      self.parties[name] = party

  def send(self, sender, receiver, message):
      if receiver in self.parties:
          self.parties[receiver].receive(sender, message)

class Party:
  def __init__(self, name, mediator):
      self.name = name
      self.mediator = mediator
      self.mediator.register(name, self)

  def send(self, receiver, message):
      self.mediator.send(self.name, receiver, message)

  def receive(self, sender, message):
      print(f"{self.name} received message from {sender}: {message}")

mediator = Mediator()
alice = Party("Alice", mediator)
bob = Party("Bob", mediator)

alice.send("Bob", "Hello Bob!")

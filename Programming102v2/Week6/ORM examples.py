Column(DateTime, default=func.now(),primary_key=True, )
department_id = Column(Integer, ForeignKey('department.id'), primary_key=True)
extra_data = Column(String(256))

User.name.property.column[0] # See the property of that column
fred = sessuin.query(User).filter_by(name="fred").one()
jack.addresses[1].user = fred # => smenq User_ID-to na adres[1] ot jack na fred


session.query(User, Adress).join(Adress, User.id == Address.user_id).all()
if we have relationship allready
session.query(User, Address).join(User.addresses).all()

reversed join:

session.query(User, Address).select_from(Address).join(Address.user).all()

from sqlalchemy import joinedload

for user in session.query(User).options(joinedload(User.addresses))
print(user, user.addresses)    => printa za vseki user vsichite mu adresi v list





class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    name = Column(String(256))


class Address(Base):
    __tablename__ = 'address'
    id = Column(Integer, primary_key=True)
    address = Column(String(256))
    user_id = Column(Integer, ForeignKey('user.id'))
    user = relationship('User', backref=backref('address', uselist=False))



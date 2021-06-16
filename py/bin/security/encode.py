from flask_bcrypt import Bcrypt

class Encode:
    bcrypt = Bcrypt()

    def hash_password(self, password):
        return self.bcrypt.generate_password_hash(password)

    def verify(self, hash, password):
        return self.bcrypt.check_password_hash(hash, password) #  True

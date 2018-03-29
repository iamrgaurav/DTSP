from passlib.hash import pbkdf2_sha512


class Utils:

    @staticmethod
    def hash_password(password):
        """
        hashes a password using pbkdf2_sha512
        :param password:The sha512 password from the login/register form
        :return:A sha512->pbkdf2 password encrypted password
        """
        return pbkdf2_sha512.encrypt(password)

    @staticmethod
    def check_hashed_password(password, hashed_password):
        """
        Checks the password the user sent matches tha password stored in the database
        The password is encrypted more than the user's password at this stage
        :param password: sha-512 hashed password
        :param hashed_password: pbkdf2_sh512 encrypted passsword
        :return: True if password matches false otherwise
        """
        return pbkdf2_sha512.verify(password, hashed_password)
import logging
import eg_api_client as eg

logging.basicConfig(
    level=logging.DEBUG,
    filename='api.log',
    filemode='w',
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%d-%m-%y %H:%M:%S'
)

if __name__ == '__main__':

    # COMMUNICO API USER CREDENTIALS
    communico_user_barcode = ''
    communico_user_password = ''

    # RETRIEVE PATRON DETAILS
    test_patron_barcode = ''
    test_patron_password = ''

    # -----------------------------------------------------------------------------------
    # EXAMPLE #1
    # -----------------------------------------------------------------------------------
    # GRAB AN AUTHENTICATION TOKEN - token operations limited to user's permission set

    authtoken = eg.retrieve_auth_token(
        {
            'barcode': communico_user_barcode,
            'password': communico_user_password,
            'type': 'opac'
         }
    )

    logging.info(f'session token is {authtoken}')

    # -----------------------------------------------------------------------------------
    # EXAMPLE #2
    # -----------------------------------------------------------------------------------
    # GET USER DETAILS - by barcode

    user_details = eg.post(
        'open-ils.actor',
        'open-ils.actor.user.fleshed.retrieve_by_barcode',
        authtoken,
        test_patron_barcode
    )

    logging.info(user_details)

    # -----------------------------------------------------------------------------------
    # EXAMPLE #3
    # -----------------------------------------------------------------------------------
    # VERIFY USER PASSWORD
    #
    # Given a barcode or username and the MD5 encoded password,
    # returns 1 if the password is correct.  Returns 0 otherwise.

    test_patron_username = ''
    t_patron_password = eg.md5_hash(test_patron_password)

    pass_check = eg.post(
        'open-ils.actor',
        'open-ils.actor.verify_user_password',
        authtoken,
        test_patron_barcode,
        test_patron_username,
        t_patron_password
    )

    logging.info(pass_check)

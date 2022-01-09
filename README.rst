moji_notif
==========

.. image:: https://img.shields.io/github/issues/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif/issues
   :alt: Issues
.. image:: https://img.shields.io/github/forks/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif
   :alt: Forks
.. image:: https://img.shields.io/github/stars/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif
   :alt: Stars
.. image:: https://img.shields.io/github/license/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif/blob/main/LICENSE
   :alt: MIT License

Moji sends text and fun facts from different APIs wit da use of a notification deamon.

Key Features
-------------

- Sends text and fun facts from different APIs:
  - history (history of wat da present month and day)
  - number_trivia (number trivias)
  - cat_fact (fun facts about cats! meow 🐱)
  - advice ('useful' advices somtimes nonsense :3)
  - random 

Installing
----------

**Python 3.8 or higher is required**

To install, you can just run the following command:

.. code:: sh

    $ git clone https://github.com/yumyumb612/moji_notif.git
    $ cd moji_notif
    $ sh install.sh # might need sudo to put da runner in /urs/bin

Required Packages
~~~~~~~~~~~~~~~~~~

* dunst or any notification deamon (moji uses notify-send)
* mpv (ringtone - it can be disabled)

Screenshots
-----------


APIs Used
---------

- `numbersapi <http://numbersapi.com>`_
- `cat-fact <https://cat-fact.herokuapp.com>`_
- `adviceslip <https://api.adviceslip.com>`_

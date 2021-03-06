moji_notif
==========

.. image:: https://img.shields.io/github/issues/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif/issues
   :alt: Issues
.. image:: https://img.shields.io/github/forks/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif
   :alt: Forks
.. image:: https://img.shields.io/github/stars/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif/stargazers
   :alt: Stars
.. image:: https://img.shields.io/github/license/yumyumb612/moji_notif
   :target: https://github.com/yumyumb612/moji_notif/blob/main/LICENSE
   :alt: MIT License

Moji sends text and fun facts from different APIs wit da use of a notification deamon. Can be runned via `dmenu <http://tools.suckless.org/dmenu/>`_ or `rofi <https://github.com/davatorium/rofi>`_.

*ps. for linux only*

Settings
-----------
Location: ~/.config/moji_notif/settings.py

The value for **api** can only be one of the following:
   - **history** - history of wat happend dis present month and day
   - **number_trivia** - random number trivias
   - **cat_fact** - fun facts about cats! meow 🐱
   - **advice** - "useful" advices, but somtimes nonsense :3
   - **random**
   
Installing
----------
**Python 3.8 or higher is required**

To install, you can just run the following command:

.. code:: sh

    $ git clone https://github.com/yumyumb612/moji_notif.git
    $ cd moji_notif
    $ sh install.sh # might need sudo to put da runner in /usr/bin

Required Packages
~~~~~~~~~~~~~~~~~~
* `dunst <https://dunst-project.org/>`_ or any notification deamon (moji uses `notify-send <https://www.commandlinux.com/man-page/man1/notify-send.1.html>`_)
* `mpv <https://mpv.io/>`_ (for ringtone - it can be disabled)

Screenshots
-----------
.. image:: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot1.png?raw=true
   :target: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot1.png?raw=true
   :alt: Screenshot1
.. image:: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot2.png?raw=true
   :target: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot2.png?raw=true
   :alt: Screenshot2
.. image:: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot3.png?raw=true
   :target: https://github.com/yumyumb612/moji_notif/blob/main/Screenshots/Screenshot3.png?raw=true
   :alt: Screenshot3

APIs Used
---------
- `numbersapi <http://numbersapi.com>`_
- `cat-fact <https://cat-fact.herokuapp.com>`_
- `adviceslip <https://api.adviceslip.com>`_

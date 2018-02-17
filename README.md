
# BeigeOrion
> An experimental project that charts Twitter bot followers. 


[![license](https://img.shields.io/github/license/mashape/apistatus.svg?style=flat-square)]()
[![Beerpay](https://img.shields.io/beerpay/jrigden/BeigeOrion.svg?style=flat-square)]()

This program will generate a website that charts Twitter bot followers for a groups of accounts. You can see a demo at [SeattleBot Labs](https://labs.seattlebot.net/2018_election/).

## Prerequisites
This program requires API keys for the [Twitter](https://apps.twitter.com/) and [Botometer](https://botometer.iuni.iu.edu/#!/api). Add those keys to the `api_keys.py` file.

## Installation

Requires Python3 and should of course be ran in some kind of virtualenv.
```sh
git clone https://github.com/jrigden/BeigeOrion.git
cd BeigeOrion
pip install -r requirements.txt
```

## Usage
Edit the `config.json` file. Then run `python beige_orion.py`.

## Release History

* 1.0.0
    * INITIAL RELEASE
   
## Errors and bugs

Report it here by creating an issue: https://github.com/jrigden/BeigeOrion/issues

## Contributors

Jason Rigden – [@mr_rigden](https://twitter.com/mr_rigden)


## Contributing

1. Fork it (<https://github.com/jrigden/BeigeOrion/fork>)
2. Create your feature branch (`git checkout -b feature/fooBar`)
3. Commit your changes (`git commit -am 'Add some fooBar'`)
4. Push to the branch (`git push origin feature/fooBar`)
5. Create a new Pull Request


## License
Distributed under the MIT license. See ``LICENSE`` for more information.

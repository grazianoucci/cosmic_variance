# Cosmic variance calculator

This is a quick and easy cosmic variance calculator based on Ucci et al. (2020), reference

[![Open Source Love](https://badges.frapsoft.com/os/v1/open-source.svg?v=103)](https://opensource.org/licenses/Apache-2.0) [![Contributions welcome](https://img.shields.io/badge/contributions-welcome-brightgreen.svg?style=flat)](https://github.com/grazianoucci/cosmic_variance/graphs/contributors)

## Prerequisites

To run the cosmic variance calculator script you need the following python packages: numpy, gzip and pickle.

## How to

We provide three simple functions that allow the user to compute the cosmic variance (expressed in percantage) for the UV Luminosity Function (UV LF), for the Stellar Mass Function (SMF), and for the Halo Mass Function (HMF).

The user should pass to the functions the following data:
- redshift
- redshift interval (i.e., z_max - z_min)
- survey area (in square arcmins)
- UV absolute magnitude / Halo mass (expressed as log10 solar masses) / Stellar mass (expressed as log10 solar masses)
- model name: 'photoionization_heating' (recommended) / 'early_heating' / 'jeans_mass'

The functions provided give as output the cosmic variance expressed in percentage.
We also provide simple examples, to get a clear idea of how to use the functions described above.

## Authors

* **Graziano Ucci** - *Kapteyn Astronomical Institute, Groningen* - [github](https://github.com/grazianoucci)

See also the list of [contributors](https://github.com/grazianoucci/cosmic_variance/contributors) who participated in this project.

## Citing

If you use this code for your work, please cite it with

* reference

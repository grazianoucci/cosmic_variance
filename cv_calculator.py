import gzip
import pickle
import numpy as np

def compute_cosmic_variance_uv(parameters, model_name, verbose=False):
    """
    This function computes the cosmic variance
    for the UV Luminosity Function (UV LF).

    The argument the user should pass is an
    array with shape (n,4) where n is the number
    of inputs for which the user wants to
    compute the cosmic variance, and the model name.
    The array should contain 4 columns:
    1st column: redshift
    2nd column: deltaz
    3rd column: survey area (in square arcmins)
    4th column: UV magnitude
    The model name could be one of the following:
    'photoionization_heating' (recommended)
    'early_heating'
    'jeans_mass'

    It returns n values for the cosmic
    variance (expressed in percentage)
    """
    # Import models previously stored
    with gzip.open('models/model_uv_'+model_name+'.pgz', 'rb') as f:
        model_uv = pickle.load(f)
    # Compute cosmic variance with interpolation
    cv = model_uv.__call__(parameters)
    if (verbose and (len(np.shape(parameters)) > 1)):
        for i in range(len(parameters)):
            print('For parameters')
            print('z           = {:.3f}'.format(parameters[i,0]))
            print('delta z     = {:.3f}'.format(parameters[i,1]))
            print('survey area = {:.3f}'.format(parameters[i,2]))
            print('UV mag      = {:.3f}'.format(parameters[i,3]))
            print('Cosmic variance is')
            print('CV          = {:.2f} %\n'.format(cv[i]))
    if (verbose and (len(np.shape(parameters)) == 1)):
        print('For parameters')
        print('z           = {:.3f}'.format(parameters[0]))
        print('delta z     = {:.3f}'.format(parameters[1]))
        print('survey area = {:.3f}'.format(parameters[2]))
        print('UV mag      = {:.3f}'.format(parameters[3]))
        print('Cosmic variance is')
        print('CV          = {:.2f} %\n'.format(float(cv)))        
    return cv

def compute_cosmic_variance_mh(parameters, model_name, verbose=False):
    """
    This function computes the cosmic variance
    for the Halo Mass Function (HMF).

    The argument the user should pass is an
    array with shape (n,4) where n is the number
    of inputs for which the user wants to
    compute the cosmic variance, and the model name.
    The array should contain 4 columns:
    1st column: redshift
    2nd column: deltaz
    3rd column: survey area (in square arcmins)
    4th column: UV magnitude
    The model name could be one of the following:
    'photoionization_heating' (recommended)
    'early_heating'
    'jeans_mass'

    It returns n values for the cosmic
    variance (expressed in percentage)
    """
    # Import models previously stored
    with gzip.open('models/model_mh_'+model_name+'.pgz', 'rb') as f:
        model_mh = pickle.load(f)
    # Compute cosmic variance with interpolation
    cv = model_mh.__call__(parameters)
    if (verbose and (len(np.shape(parameters)) > 1)):
        for i in range(len(parameters)):
            print('For parameters')
            print('z           = {:.3f}'.format(parameters[i,0]))
            print('delta z     = {:.3f}'.format(parameters[i,1]))
            print('survey area = {:.3f}'.format(parameters[i,2]))
            print('Halo Mass   = {:.3f}'.format(parameters[i,3]))
            print('Cosmic variance is')
            print('CV          = {:.2f} %\n'.format(cv[i]))
    if (verbose and (len(np.shape(parameters)) == 1)):
        print('For parameters')
        print('z           = {:.3f}'.format(parameters[0]))
        print('delta z     = {:.3f}'.format(parameters[1]))
        print('survey area = {:.3f}'.format(parameters[2]))
        print('Halo Mass   = {:.3f}'.format(parameters[3]))
        print('Cosmic variance is')
        print('CV          = {:.2f} %\n'.format(float(cv)))        
    return cv

def compute_cosmic_variance_ms(parameters, model_name, verbose=False):
    """
    This function computes the cosmic variance
    for the Stellar Mass Function (SMF).

    The argument the user should pass is an
    array with shape (n,4) where n is the number
    of inputs for which the user wants to
    compute the cosmic variance, and the model name.
    The array should contain 4 columns:
    1st column: redshift
    2nd column: deltaz
    3rd column: survey area (in square arcmins)
    4th column: UV magnitude
    The model name could be one of the following:
    'photoionization_heating' (recommended)
    'early_heating'
    'jeans_mass'

    It returns n values for the cosmic
    variance (expressed in percentage)
    """
    # Import models previously stored
    with gzip.open('models/model_ms_'+model_name+'.pgz', 'rb') as f:
        model_ms = pickle.load(f)
    # Compute cosmic variance with interpolation
    cv = model_ms.__call__(parameters)
    if (verbose and (len(np.shape(parameters)) > 1)):
        for i in range(len(parameters)):
            print('For parameters')
            print('z            = {:.3f}'.format(parameters[i,0]))
            print('delta z      = {:.3f}'.format(parameters[i,1]))
            print('survey area  = {:.3f}'.format(parameters[i,2]))
            print('Stellar Mass = {:.3f}'.format(parameters[i,3]))
            print('Cosmic variance is')
            print('CV           = {:.2f} %\n'.format(cv[i]))
    if (verbose and (len(np.shape(parameters)) == 1)):
        print('For parameters')
        print('z            = {:.3f}'.format(parameters[0]))
        print('delta z      = {:.3f}'.format(parameters[1]))
        print('survey area  = {:.3f}'.format(parameters[2]))
        print('Stellar Mass = {:.3f}'.format(parameters[3]))
        print('Cosmic variance is')
        print('CV           = {:.2f} %\n'.format(float(cv)))        
    return cv

######################
# Some EXAMPLE tests #
######################
test_uv1 = np.array([[8.65, 0.125, 82.5, -16],
                     [8.01, 0.125, 42.5, -17],
                     [9.52, 0.150, 13.5, -18],
                     [8.65, 0.125, 120,  -20],
                     [8.00, 0.125, 82.5, -18]])
test_uv2 = np.array( [8.12, 0.625, 58.5, -17])
cv_uv1   = compute_cosmic_variance_uv(test_uv1, 'photoionization_heating')
cv_uv2   = compute_cosmic_variance_uv(test_uv2, 'photoionization_heating', verbose=True)        
test_mh1 = np.array([[8.65, 0.125, 82.5, 10.0],
                     [8.01, 0.125, 42.5, 10.5],
                     [9.52, 0.150, 13.5, 11.2],
                     [8.65, 0.125, 120,  9.81],
                     [8.00, 0.125, 82.5, 10.0]])
test_mh2 = np.array( [8.12, 0.625, 58.5, 10.5])
cv_mh1   = compute_cosmic_variance_mh(test_mh1, 'early_heating')
cv_mh2   = compute_cosmic_variance_mh(test_mh2, 'early_heating')
print(cv_mh1)
print(cv_mh2)
test_ms1 = np.array([[8.65, 0.125, 82.5, 7.0],
                     [8.01, 0.125, 42.5, 8.5],
                     [9.52, 0.150, 13.5, 7.2],
                     [8.65, 0.125, 120,  7.8],
                     [8.00, 0.125, 82.5, 8.0]])
test_ms2 = np.array( [8.12, 0.625, 58.5, 8.5])
cv_ms1   = compute_cosmic_variance_ms(test_ms1, 'jeans_mass', verbose=True)
cv_ms2   = compute_cosmic_variance_ms(test_ms2, 'jeans_mass')
print(cv_ms1)
print(cv_ms2)

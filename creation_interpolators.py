import pickle
from scipy.interpolate import LinearNDInterpolator

# Read UV magnitudes data
data_uv = np.loadtxt('cosmic_variance_tables/matrix_cosmic_variance_uv.dat')
# Linear interpolator UV magnitudes
linint_uv = LinearNDInterpolator(data_uv[:,:4], data_uv[:,4])
# Save interpolator UV magnitudes
with open('interpolators/interpolator_uv.pkl', 'wb') as f:
    pickle.dump(linint_uv, f)

# Read HALO mass data
data_mh = np.loadtxt('cosmic_variance_tables/matrix_cosmic_variance_mh.dat')
# Linear interpolator HALO mass
linint_mh = LinearNDInterpolator(data_mh[:,:4], data_mh[:,4])
# Save interpolator HALO mass
with open('interpolators/interpolator_mh.pkl', 'wb') as f:
    pickle.dump(linint_mh, f)

# Read STELLAR mass data
data_ms = np.loadtxt('cosmic_variance_tables/matrix_cosmic_variance_ms.dat')
# Linear interpolator STELLAR mass
linint_ms = LinearNDInterpolator(data_ms[:,:4], data_ms[:,4])
# Save interpolator STELLAR mass
with open('interpolators/interpolator_ms.pkl', 'wb') as f:
    pickle.dump(linint_ms, f)

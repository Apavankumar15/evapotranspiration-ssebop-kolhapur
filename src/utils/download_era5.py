import cdsapi

print("Connecting to CDS API...")

c = cdsapi.Client()

print("Connected. Submitting ERA5-Land request...")

c.retrieve(
    'reanalysis-era5-land',


    {
        'variable': [
            '2m_temperature',
            '2m_dewpoint_temperature',
            '10m_u_component_of_wind',
            '10m_v_component_of_wind',
            'surface_net_solar_radiation',
            'surface_net_thermal_radiation',
        ],
        'year': '2023',
        'month': [f"{m:02d}" for m in range(1, 13)],
        'day': [f"{d:02d}" for d in range(1, 32)],
        'time': '12:00',
        'area': [
            17.2, 73.6,   # North, West
            15.7, 74.8    # South, East (Kolhapur)
        ],
        'format': 'netcdf',
    },
    'data/raw/era5_kolhapur_2023.nc'
)

print("ERA5-Land download COMPLETED")

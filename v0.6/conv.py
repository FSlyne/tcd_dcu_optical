
import ast

data_string = "{'ImpTF200g16QNorm_indefinite_sop-tracking': '69', 'CarrierTF_indefinite_opt-rcv-pwr': '-4.9', 'Carrier_15min_opt-rcv-pwr-lo': '-5.6', 'Carrier_15min_opt-rcv-pwr-mean': '-5.0', 'Carrier_15min_opt-rcv-pwr-hi': '-4.6', 'Carrier_24hour_opt-rcv-pwr-lo': '-43.7', 'Carrier_24hour_opt-rcv-pwr-mean': '-8.4', 'Carrier_24hour_opt-rcv-pwr-hi': '-4.6', 'QualityTF_indefinite_carrier-frequency-offset': '-0.019', 'QualityTF_indefinite_q-factor': '12.0', 'QualityTF_indefinite_polarization-dependent-loss': '0.4', 'Quality_15min_carrier-frequency-offset-lo': '-0.036', 'Quality_15min_carrier-frequency-offset-mean': '0.002', 'Quality_15min_carrier-frequency-offset-hi': '0.038', 'Quality_15min_q-factor-lo': '11.9', 'Quality_15min_q-factor-mean': '12.0', 'Quality_15min_q-factor-hi': '12.0', 'Quality_15min_polarization-dependent-loss-lo': '0.3', 'Quality_15min_polarization-dependent-loss-mean': '0.4', 'Quality_15min_polarization-dependent-loss-hi': '0.5', 'Quality_24hour_carrier-frequency-offset-lo': '-0.039', 'Quality_24hour_carrier-frequency-offset-mean': '0.0', 'Quality_24hour_carrier-frequency-offset-hi': '0.039', 'Quality_24hour_q-factor-lo': '0.0', 'Quality_24hour_q-factor-mean': '11.6', 'Quality_24hour_q-factor-hi': '12.1', 'Quality_24hour_polarization-dependent-loss-lo': '0.0', 'Quality_24hour_polarization-dependent-loss-mean': '0.5', 'Quality_24hour_polarization-dependent-loss-hi': '1.2', 'QualityTF200g16Q_indefinite_signal-to-noise-ratio': '19.1', 'QualityTF200g16Q_indefinite_optical-signal-to-noise-ratio': '26.8', 'QualityTF200g16Q_indefinite_differential-group-delay': '3', 'QualityMod_15min_signal-to-noise-ratio-lo': '18.8', 'QualityMod_15min_signal-to-noise-ratio-mean': '19.1', 'QualityMod_15min_signal-to-noise-ratio-hi': '19.3', 'QualityMod_15min_optical-signal-to-noise-ratio-lo': '26.3', 'QualityMod_15min_optical-signal-to-noise-ratio-mean': '26.8', 'QualityMod_15min_optical-signal-to-noise-ratio-hi': '27.1', 'QualityMod_15min_differential-group-delay-lo': '2', 'QualityMod_15min_differential-group-delay-mean': '3', 'QualityMod_15min_differential-group-delay-hi': '4', 'QualityMod_24hour_signal-to-noise-ratio-lo': '0.0', 'QualityMod_24hour_signal-to-noise-ratio-mean': '18.6', 'QualityMod_24hour_signal-to-noise-ratio-hi': '19.3', 'QualityMod_24hour_optical-signal-to-noise-ratio-lo': '0.0', 'QualityMod_24hour_optical-signal-to-noise-ratio-mean': '25.6', 'QualityMod_24hour_optical-signal-to-noise-ratio-hi': '35.4', 'QualityMod_24hour_differential-group-delay-lo': '0', 'QualityMod_24hour_differential-group-delay-mean': '3', 'QualityMod_24hour_differential-group-delay-hi': '5', 'ImpCdc_15min_chromatic-dispersion-compensation-lo': '-3228', 'ImpCdc_15min_chromatic-dispersion-compensation-mean': '-3217', 'ImpCdc_15min_chromatic-dispersion-compensation-hi': '-3205', 'ImpCdc_24hour_chromatic-dispersion-compensation-lo': '-3236', 'ImpCdc_24hour_chromatic-dispersion-compensation-mean': '-3202', 'ImpCdc_24hour_chromatic-dispersion-compensation-hi': '0', 'Impairments_15min_sop-tracking-lo': '0', 'Impairments_15min_sop-tracking-mean': '18', 'Impairments_15min_sop-tracking-hi': '87', 'Impairments_24hour_sop-tracking-lo': '0', 'Impairments_24hour_sop-tracking-mean': '22', 'Impairments_24hour_sop-tracking-hi': '95', 'ImpTF16QCdcRange2_indefinite_chromatic-dispersion-compensation': '-3210'}"

perf_dict = ast.literal_eval(data_string)

print("Optical Receive Power, Q-Factor, SNR, OSNR, FEC ber")
print(perf_dict['CarrierTF_indefinite_opt-rcv-pwr'],
perf_dict['QualityTF_indefinite_q-factor'],
perf_dict['QualityTF200g16Q_indefinite_signal-to-noise-ratio'],
perf_dict['QualityTF200g16Q_indefinite_optical-signal-to-noise-ratio'],
# '{:.2e}'.format(float( perf_dict['FEC:indefinite:fec-ber'])),
# perf_dict['FEC:15min:fec-uncorrected-blocks']
)
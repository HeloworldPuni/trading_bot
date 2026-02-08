//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_MA_Cross_SMA, L_Money_Flow_Index
// ID_model: MSFT_30Min_2MM0_6c8d8263 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_MSFT_30Min_2MM0_6c8d8263", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_MSFT_30Min_6c8d8263(Short_MA, Long_MA, Short_Long_Diff, MA_Cross, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(max_depth=8, max_features=sqrt, min_samples_leaf=7,min_samples_split=5, random_state=843828734)
	if( Negative_Money_Flow_Sum <= 1.52504e+08 )
		if( Short_Long_Diff <= 0.845591 )
			if( Raw_Money_Flow <= 1.31965e+07 )
				if( MFI_High <= -52.4468 )
					if( Positive_Money_Flow_Sum <= 1.31278e+06 )
						if( Raw_Money_Flow <= 1.02176e+06 )
							if( Negative_Money_Flow_Sum <= 3.40303e+06 )
								ret := 0.363636
							if( Negative_Money_Flow_Sum > 3.40303e+06 )
								ret := -0.300000
						if( Raw_Money_Flow > 1.02176e+06 )
							if( Negative_Money_Flow <= 1.71602e+06 )
								if( Negative_Money_Flow <= 1.30642e+06 )
									ret := 0.928571 // buy
								if( Negative_Money_Flow > 1.30642e+06 )
									ret := 0.545455
							if( Negative_Money_Flow > 1.71602e+06 )
								if( Raw_Money_Flow <= 2.61274e+06 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 2.61274e+06 )
									ret := 0.888889 // buy
					if( Positive_Money_Flow_Sum > 1.31278e+06 )
						if( Typical_Price <= 80.4002 )
							if( MFI_Low <= 0.57042 )
								if( MFI_Low <= -7.97367 )
									ret := -0.818182 // sell
								if( MFI_Low > -7.97367 )
									ret := -1.000000 // sell
							if( MFI_Low > 0.57042 )
								ret := -0.250000
						if( Typical_Price > 80.4002 )
							if( Negative_Money_Flow_Sum <= 1.04864e+08 )
								if( Positive_Money_Flow_Sum <= 1.72001e+07 )
									ret := 0.097696
								if( Positive_Money_Flow_Sum > 1.72001e+07 )
									ret := 0.710526 // buy
							if( Negative_Money_Flow_Sum > 1.04864e+08 )
								if( Typical_Price <= 210.058 )
									ret := -0.347826
								if( Typical_Price > 210.058 )
									ret := -0.777778 // sell
				if( MFI_High > -52.4468 )
					if( Short_MA <= 50.3672 )
						if( MFI_Low <= 73.2106 )
							if( Typical_Price <= 49.4344 )
								ret := 1.000000 // buy
							if( Typical_Price > 49.4344 )
								ret := 0.538462
						if( MFI_Low > 73.2106 )
							ret := 0.058824
					if( Short_MA > 50.3672 )
						if( Positive_Money_Flow <= 48279.5 )
							if( Raw_Money_Flow <= 3.01649e+06 )
								if( Long_MA <= 140.553 )
									ret := -0.087349
								if( Long_MA > 140.553 )
									ret := 0.168919
							if( Raw_Money_Flow > 3.01649e+06 )
								if( Negative_Money_Flow_Sum <= 1.22424e+07 )
									ret := -0.279503
								if( Negative_Money_Flow_Sum > 1.22424e+07 )
									ret := -0.078792
						if( Positive_Money_Flow > 48279.5 )
							if( Short_Long_Diff <= -0.016017 )
								if( Money_Flow_Ratio <= 52.7554 )
									ret := -0.087948
								if( Money_Flow_Ratio > 52.7554 )
									ret := 0.174757
							if( Short_Long_Diff > -0.016017 )
								if( Positive_Money_Flow <= 1.31958e+06 )
									ret := -0.310475
								if( Positive_Money_Flow > 1.31958e+06 )
									ret := -0.104609
			if( Raw_Money_Flow > 1.31965e+07 )
				if( MFI_High <= -39.5908 )
					if( Typical_Price <= 233.097 )
						if( Negative_Money_Flow_Sum <= 5.20739e+07 )
							if( MFI_High <= -56.5637 )
								if( Typical_Price <= 114.825 )
									ret := 0.466667
								if( Typical_Price > 114.825 )
									ret := -0.407407
							if( MFI_High > -56.5637 )
								if( MFI_High <= -44.3866 )
									ret := 0.866667 // buy
								if( MFI_High > -44.3866 )
									ret := 0.133333
						if( Negative_Money_Flow_Sum > 5.20739e+07 )
							if( Typical_Price <= 129.464 )
								ret := -0.333333
							if( Typical_Price > 129.464 )
								if( Raw_Money_Flow <= 1.72952e+07 )
									ret := 0.965517 // buy
								if( Raw_Money_Flow > 1.72952e+07 )
									ret := 0.672515
					if( Typical_Price > 233.097 )
						if( Positive_Money_Flow_Sum <= 1.61662e+07 )
							if( Money_Flow_Ratio <= 0.525058 )
								if( MFI_Low <= -2.54835 )
									ret := 0.237037
								if( MFI_Low > -2.54835 )
									ret := 0.610465
							if( Money_Flow_Ratio > 0.525058 )
								ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 1.61662e+07 )
							if( Raw_Money_Flow <= 1.25281e+08 )
								if( MFI_Low <= 15.6029 )
									ret := -0.148810
								if( MFI_Low > 15.6029 )
									ret := 0.335526
							if( Raw_Money_Flow > 1.25281e+08 )
								ret := -1.000000 // sell
				if( MFI_High > -39.5908 )
					if( Long_MA <= 237.634 )
						if( Negative_Money_Flow_Sum <= 9.89101e+07 )
							if( Negative_Money_Flow <= 1.23627e+06 )
								if( Money_Flow_Ratio <= 508.471 )
									ret := 0.030047
								if( Money_Flow_Ratio > 508.471 )
									ret := 0.384342
							if( Negative_Money_Flow > 1.23627e+06 )
								if( Negative_Money_Flow_Sum <= 2.96865e+07 )
									ret := -0.181818
								if( Negative_Money_Flow_Sum > 2.96865e+07 )
									ret := 0.394928
						if( Negative_Money_Flow_Sum > 9.89101e+07 )
							if( MFI_High <= -3.20636 )
								if( MFI_High <= -3.96789 )
									ret := -0.281879
								if( MFI_High > -3.96789 )
									ret := -0.800000 // sell
							if( MFI_High > -3.20636 )
								if( MFI <= 95.0084 )
									ret := 0.043578
								if( MFI > 95.0084 )
									ret := -0.777778 // sell
					if( Long_MA > 237.634 )
						if( MFI_High <= 8.1349 )
							if( Positive_Money_Flow <= 4.70953e+07 )
								if( Positive_Money_Flow_Sum <= 2.82215e+07 )
									ret := -0.662069
								if( Positive_Money_Flow_Sum > 2.82215e+07 )
									ret := -0.075670
							if( Positive_Money_Flow > 4.70953e+07 )
								if( Long_MA <= 317.544 )
									ret := -0.384615
								if( Long_MA > 317.544 )
									ret := -0.878049 // sell
						if( MFI_High > 8.1349 )
							if( MFI <= 99.6775 )
								if( Short_MA <= 311.708 )
									ret := -0.103343
								if( Short_MA > 311.708 )
									ret := 0.122835
							if( MFI > 99.6775 )
								if( Long_MA <= 264.053 )
									ret := -0.880000 // sell
								if( Long_MA > 264.053 )
									ret := -0.333333
		if( Short_Long_Diff > 0.845591 )
			if( Short_MA <= 166.579 )
				if( MFI_High <= -36.6553 )
					if( Positive_Money_Flow_Sum <= 1.53643e+07 )
						ret := 0.545455
					if( Positive_Money_Flow_Sum > 1.53643e+07 )
						ret := -0.181818
				if( MFI_High > -36.6553 )
					if( Raw_Money_Flow <= 8.65156e+07 )
						if( Typical_Price <= 145.142 )
							if( MFI_High <= 19.6524 )
								if( Long_MA <= 83.8266 )
									ret := 0.583333
								if( Long_MA > 83.8266 )
									ret := -0.435644
							if( MFI_High > 19.6524 )
								ret := 0.333333
						if( Typical_Price > 145.142 )
							if( Raw_Money_Flow <= 1.03564e+07 )
								ret := -1.000000 // sell
							if( Raw_Money_Flow > 1.03564e+07 )
								if( Negative_Money_Flow_Sum <= 5.16849e+07 )
									ret := 0.000000
								if( Negative_Money_Flow_Sum > 5.16849e+07 )
									ret := -0.851064 // sell
					if( Raw_Money_Flow > 8.65156e+07 )
						if( Typical_Price <= 146.427 )
							if( MFI_High <= 16.3849 )
								ret := 0.214286
							if( MFI_High > 16.3849 )
								ret := -0.235294
						if( Typical_Price > 146.427 )
							ret := 0.900000 // buy
			if( Short_MA > 166.579 )
				if( Raw_Money_Flow <= 1.70309e+06 )
					if( Short_MA <= 189.981 )
						ret := 0.125000
					if( Short_MA > 189.981 )
						if( Short_Long_Diff <= 1.07048 )
							if( Positive_Money_Flow_Sum <= 3.05985e+09 )
								if( Negative_Money_Flow_Sum <= 1.23158e+07 )
									ret := -0.227273
								if( Negative_Money_Flow_Sum > 1.23158e+07 )
									ret := -0.720000 // sell
							if( Positive_Money_Flow_Sum > 3.05985e+09 )
								if( MFI <= 99.615 )
									ret := -0.193548
								if( MFI > 99.615 )
									ret := 0.290323
						if( Short_Long_Diff > 1.07048 )
							if( MFI_High <= 19.57 )
								if( Negative_Money_Flow_Sum <= 3.8307e+07 )
									ret := -0.745098 // sell
								if( Negative_Money_Flow_Sum > 3.8307e+07 )
									ret := -0.333333
							if( MFI_High > 19.57 )
								if( Positive_Money_Flow <= 273170 )
									ret := -0.044444
								if( Positive_Money_Flow > 273170 )
									ret := -0.564516
				if( Raw_Money_Flow > 1.70309e+06 )
					if( Positive_Money_Flow_Sum <= 6.19847e+07 )
						if( MFI_High <= -7.87324 )
							if( Money_Flow_Ratio <= 1.45966 )
								if( Short_Long_Diff <= 0.927939 )
									ret := -0.340000
								if( Short_Long_Diff > 0.927939 )
									ret := 0.062300
							if( Money_Flow_Ratio > 1.45966 )
								if( Short_Long_Diff <= 1.22227 )
									ret := -0.427083
								if( Short_Long_Diff > 1.22227 )
									ret := -0.101449
						if( MFI_High > -7.87324 )
							if( MFI_High <= -0.419765 )
								if( MFI_High <= -5.47236 )
									ret := 0.294118
								if( MFI_High > -5.47236 )
									ret := 0.730769 // buy
							if( MFI_High > -0.419765 )
								if( Positive_Money_Flow <= 1.4663e+07 )
									ret := 0.333333
								if( Positive_Money_Flow > 1.4663e+07 )
									ret := -0.500000
					if( Positive_Money_Flow_Sum > 6.19847e+07 )
						if( MFI_High <= -1.86342 )
							if( Raw_Money_Flow <= 1.67086e+07 )
								if( Raw_Money_Flow <= 9.47711e+06 )
									ret := -0.500000
								if( Raw_Money_Flow > 9.47711e+06 )
									ret := 0.250000
							if( Raw_Money_Flow > 1.67086e+07 )
								if( Positive_Money_Flow_Sum <= 1.2575e+08 )
									ret := -0.633166
								if( Positive_Money_Flow_Sum > 1.2575e+08 )
									ret := -0.050847
						if( MFI_High > -1.86342 )
							if( Money_Flow_Ratio <= 488.276 )
								if( MFI <= 93.5496 )
									ret := 0.148148
								if( MFI > 93.5496 )
									ret := -0.218889
							if( Money_Flow_Ratio > 488.276 )
								if( Typical_Price <= 322.546 )
									ret := 0.540541
								if( Typical_Price > 322.546 )
									ret := -0.393939
	if( Negative_Money_Flow_Sum > 1.52504e+08 )
		if( MFI_Low <= -15.4963 )
			if( Short_MA <= 214.927 )
				if( Positive_Money_Flow_Sum <= 3.45477e+07 )
					if( Typical_Price <= 51.1667 )
						if( MFI <= 0.789171 )
							if( Negative_Money_Flow_Sum <= 5.51832e+08 )
								if( Short_Long_Diff <= 0.008454 )
									ret := 0.933333 // buy
								if( Short_Long_Diff > 0.008454 )
									ret := 0.900000 // buy
							if( Negative_Money_Flow_Sum > 5.51832e+08 )
								ret := 0.181818
						if( MFI > 0.789171 )
							if( MFI_Low <= -18.9989 )
								ret := -0.384615
							if( MFI_Low > -18.9989 )
								ret := 0.800000 // buy
					if( Typical_Price > 51.1667 )
						if( Raw_Money_Flow <= 1.46318e+08 )
							if( Positive_Money_Flow <= 422.492 )
								if( Raw_Money_Flow <= 1.39638e+08 )
									ret := 0.171537
								if( Raw_Money_Flow > 1.39638e+08 )
									ret := 0.547619
							if( Positive_Money_Flow > 422.492 )
								if( Positive_Money_Flow <= 266298 )
									ret := -0.339683
								if( Positive_Money_Flow > 266298 )
									ret := 0.074074
						if( Raw_Money_Flow > 1.46318e+08 )
							if( Raw_Money_Flow <= 2.84766e+08 )
								if( Negative_Money_Flow <= 1.49699e+08 )
									ret := -1.000000 // sell
								if( Negative_Money_Flow > 1.49699e+08 )
									ret := -0.214626
							if( Raw_Money_Flow > 2.84766e+08 )
								if( Short_MA <= 94.5289 )
									ret := 0.335878
								if( Short_MA > 94.5289 )
									ret := -0.077519
				if( Positive_Money_Flow_Sum > 3.45477e+07 )
					if( Raw_Money_Flow <= 2.67535e+06 )
						if( MFI_Low <= -17.3824 )
							if( MFI_High <= -78.0229 )
								if( Short_Long_Diff <= 0.239102 )
									ret := 0.400000
								if( Short_Long_Diff > 0.239102 )
									ret := -0.900000 // sell
							if( MFI_High > -78.0229 )
								ret := -0.647059
						if( MFI_Low > -17.3824 )
							if( Short_Long_Diff <= -0.245034 )
								ret := 0.800000 // buy
							if( Short_Long_Diff > -0.245034 )
								if( Short_Long_Diff <= 0.073562 )
									ret := 0.066667
								if( Short_Long_Diff > 0.073562 )
									ret := -0.444444
					if( Raw_Money_Flow > 2.67535e+06 )
						if( Money_Flow_Ratio <= 0.037336 )
							if( Short_Long_Diff <= 0.136561 )
								if( Short_Long_Diff <= -0.791739 )
									ret := 0.909091 // buy
								if( Short_Long_Diff > -0.791739 )
									ret := 0.623077
							if( Short_Long_Diff > 0.136561 )
								if( Negative_Money_Flow_Sum <= 2.19756e+09 )
									ret := 0.478261
								if( Negative_Money_Flow_Sum > 2.19756e+09 )
									ret := -0.192308
						if( Money_Flow_Ratio > 0.037336 )
							if( Long_MA <= 173.185 )
								if( Positive_Money_Flow_Sum <= 5.04842e+07 )
									ret := 0.687500
								if( Positive_Money_Flow_Sum > 5.04842e+07 )
									ret := -0.062500
							if( Long_MA > 173.185 )
								if( Short_Long_Diff <= 0.338446 )
									ret := -0.080000
								if( Short_Long_Diff > 0.338446 )
									ret := -0.571429
			if( Short_MA > 214.927 )
				if( Positive_Money_Flow <= 1.28836e+07 )
					if( Raw_Money_Flow <= 4.55111e+08 )
						if( Long_MA <= 324.6 )
							if( MFI_High <= -77.9478 )
								if( Short_MA <= 259.505 )
									ret := 0.001486
								if( Short_MA > 259.505 )
									ret := -0.217905
							if( MFI_High > -77.9478 )
								if( Typical_Price <= 284.239 )
									ret := -0.445055
								if( Typical_Price > 284.239 )
									ret := -0.025316
						if( Long_MA > 324.6 )
							if( Typical_Price <= 411.39 )
								if( MA_Cross <= 27.6367 )
									ret := 0.196970
								if( MA_Cross > 27.6367 )
									ret := -0.600000
							if( Typical_Price > 411.39 )
								if( MFI_High <= -75.683 )
									ret := -0.046512
								if( MFI_High > -75.683 )
									ret := -0.909091 // sell
					if( Raw_Money_Flow > 4.55111e+08 )
						if( Short_Long_Diff <= -3.16274 )
							if( Short_MA <= 343.896 )
								if( Short_Long_Diff <= -3.49791 )
									ret := 1.000000 // buy
								if( Short_Long_Diff > -3.49791 )
									ret := 0.250000
							if( Short_MA > 343.896 )
								ret := 0.000000
						if( Short_Long_Diff > -3.16274 )
							if( Positive_Money_Flow_Sum <= 3.02347e+07 )
								if( Money_Flow_Ratio <= 0.006309 )
									ret := -0.046296
								if( Money_Flow_Ratio > 0.006309 )
									ret := -0.452489
							if( Positive_Money_Flow_Sum > 3.02347e+07 )
								if( Typical_Price <= 372.928 )
									ret := -0.070261
								if( Typical_Price > 372.928 )
									ret := -0.515723
				if( Positive_Money_Flow > 1.28836e+07 )
					if( MFI <= 2.86559 )
						if( MFI <= 2.07483 )
							ret := 0.652174
						if( MFI > 2.07483 )
							ret := 1.000000 // buy
					if( MFI > 2.86559 )
						ret := 0.357143
		if( MFI_Low > -15.4963 )
			if( Positive_Money_Flow <= 4.27458e+08 )
				if( Short_MA <= 48.4883 )
					ret := 0.857143 // buy
				if( Short_MA > 48.4883 )
					if( Short_Long_Diff <= -3.76847 )
						if( Negative_Money_Flow <= 3.02113e+08 )
							if( Positive_Money_Flow <= 1.70018e+07 )
								if( Long_MA <= 329.268 )
									ret := -0.388235
								if( Long_MA > 329.268 )
									ret := 0.314286
							if( Positive_Money_Flow > 1.70018e+07 )
								if( Positive_Money_Flow <= 8.08222e+07 )
									ret := 0.757576 // buy
								if( Positive_Money_Flow > 8.08222e+07 )
									ret := 0.058824
						if( Negative_Money_Flow > 3.02113e+08 )
							if( Positive_Money_Flow_Sum <= 2.57528e+09 )
								if( Typical_Price <= 231.357 )
									ret := -0.214286
								if( Typical_Price > 231.357 )
									ret := 0.543860
							if( Positive_Money_Flow_Sum > 2.57528e+09 )
								ret := 1.000000 // buy
					if( Short_Long_Diff > -3.76847 )
						if( Raw_Money_Flow <= 6.1025e+08 )
							if( MA_Cross <= 3.04759 )
								if( Positive_Money_Flow <= 46312.4 )
									ret := 0.057717
								if( Positive_Money_Flow > 46312.4 )
									ret := -0.001186
							if( MA_Cross > 3.04759 )
								if( MFI_Low <= 51.2968 )
									ret := 0.212101
								if( MFI_Low > 51.2968 )
									ret := -0.089939
						if( Raw_Money_Flow > 6.1025e+08 )
							if( Long_MA <= 265.571 )
								if( MFI <= 68.0313 )
									ret := 0.028525
								if( MFI > 68.0313 )
									ret := 0.495050
							if( Long_MA > 265.571 )
								if( Negative_Money_Flow_Sum <= 5.22299e+09 )
									ret := -0.096654
								if( Negative_Money_Flow_Sum > 5.22299e+09 )
									ret := -0.340845
			if( Positive_Money_Flow > 4.27458e+08 )
				if( MFI_High <= -42.8301 )
					if( MFI_Low <= -5.30667 )
						if( Positive_Money_Flow_Sum <= 8.6287e+08 )
							if( MFI <= 14.1325 )
								if( MFI <= 8.97484 )
									ret := 0.785714 // buy
								if( MFI > 8.97484 )
									ret := -0.541667
							if( MFI > 14.1325 )
								ret := 0.750000 // buy
						if( Positive_Money_Flow_Sum > 8.6287e+08 )
							if( Short_Long_Diff <= -4.63142 )
								ret := 1.000000 // buy
							if( Short_Long_Diff > -4.63142 )
								ret := 0.400000
					if( MFI_Low > -5.30667 )
						if( Raw_Money_Flow <= 5.10362e+08 )
							if( MFI_High <= -47.6124 )
								if( MFI_High <= -50.459 )
									ret := -0.125926
								if( MFI_High > -50.459 )
									ret := -0.765957 // sell
							if( MFI_High > -47.6124 )
								if( Positive_Money_Flow <= 5.01904e+08 )
									ret := 0.100000
								if( Positive_Money_Flow > 5.01904e+08 )
									ret := 1.000000 // buy
						if( Raw_Money_Flow > 5.10362e+08 )
							if( Short_Long_Diff <= -0.308516 )
								if( Raw_Money_Flow <= 6.81676e+08 )
									ret := -0.383929
								if( Raw_Money_Flow > 6.81676e+08 )
									ret := 0.045226
							if( Short_Long_Diff > -0.308516 )
								if( Typical_Price <= 364.224 )
									ret := -0.737500 // sell
								if( Typical_Price > 364.224 )
									ret := -0.333333
				if( MFI_High > -42.8301 )
					if( Positive_Money_Flow_Sum <= 2.03969e+09 )
						if( Long_MA <= 236.644 )
							if( Positive_Money_Flow <= 6.47409e+08 )
								if( Raw_Money_Flow <= 5.00552e+08 )
									ret := 0.125000
								if( Raw_Money_Flow > 5.00552e+08 )
									ret := 0.489655
							if( Positive_Money_Flow > 6.47409e+08 )
								if( MFI_Low <= 19.3176 )
									ret := 0.800000 // buy
								if( MFI_Low > 19.3176 )
									ret := -0.060241
						if( Long_MA > 236.644 )
							if( MFI <= 70.2767 )
								if( Positive_Money_Flow_Sum <= 6.57039e+08 )
									ret := -0.553571
								if( Positive_Money_Flow_Sum > 6.57039e+08 )
									ret := -0.033755
							if( MFI > 70.2767 )
								if( Raw_Money_Flow <= 1.49441e+09 )
									ret := 0.240000
								if( Raw_Money_Flow > 1.49441e+09 )
									ret := 0.904762 // buy
					if( Positive_Money_Flow_Sum > 2.03969e+09 )
						if( Positive_Money_Flow_Sum <= 2.71666e+09 )
							if( Raw_Money_Flow <= 1.77974e+09 )
								if( MFI_Low <= 55.9595 )
									ret := -0.243363
								if( MFI_Low > 55.9595 )
									ret := 0.153153
							if( Raw_Money_Flow > 1.77974e+09 )
								ret := -1.000000 // sell
						if( Positive_Money_Flow_Sum > 2.71666e+09 )
							if( Positive_Money_Flow_Sum <= 5.09288e+09 )
								if( Positive_Money_Flow_Sum <= 4.33598e+09 )
									ret := -0.061420
								if( Positive_Money_Flow_Sum > 4.33598e+09 )
									ret := 0.233918
							if( Positive_Money_Flow_Sum > 5.09288e+09 )
								if( MFI_High <= -4.58649 )
									ret := -0.279487
								if( MFI_High > -4.58649 )
									ret := -0.064677
	
    ret //return
// Define expected timeframe based on the selected interval: 30Min pine_value: 30   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  30MIN !!"
if (str.tostring(timeframe.period) != "30")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_MA_Cross_SMA 
//@version=5
//indicator title="MA Cross", overlay=true)

shortlen = input.int(9, title="Short MA Length", minval=1)
longlen = input.int(21, title="Long MA Length", minval=1)

// Calculate the short and long simple moving averages (SMA)
Short_MA = ta.sma(close, shortlen)
Long_MA = ta.sma(close, longlen)

// Calculate the difference between short MA and long MA
Short_Long_Diff = Short_MA - Long_MA

// Identify crossover points where short MA crosses above or below the long MA
MA_Cross = ta.valuewhen(ta.crossover(Short_MA, Long_MA), Short_MA, 0)

// Plot the results
plot(Short_MA, color=color.orange, title="Short MA")
plot(Long_MA, color=color.green, title="Long MA")
plotshape(na(MA_Cross) ? na : MA_Cross, style=shape.cross, location=location.absolute, color=color.blue, title="Cross")


//CODE associated with the technical indicator L_Money_Flow_Index 
//@version=5
//indicator title="Money Flow Index (MFI)", shorttitle="MFI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)

// Input parameters
length_MFI = input.int(14, minval=1, title="MFI Length")

// Calculate the Typical Price
Typical_Price = (high + low + close) / 3

// Calculate Raw Money Flow
Raw_Money_Flow = Typical_Price * volume

// Calculate Positive and Negative Money Flow
Positive_Money_Flow = Raw_Money_Flow * (Typical_Price > Typical_Price[1] ? 1 : 0)
Negative_Money_Flow = Raw_Money_Flow * (Typical_Price < Typical_Price[1] ? 1 : 0)

// Sum of Positive and Negative Money Flow over the given length
Positive_Money_Flow_Sum = ta.sma(Positive_Money_Flow, length_MFI) * length_MFI
Negative_Money_Flow_Sum = ta.sma(Negative_Money_Flow, length_MFI) * length_MFI

// Calculate Money Flow Ratio
Money_Flow_Ratio = Positive_Money_Flow_Sum / Negative_Money_Flow_Sum

// Calculate MFI
MFI = 100 - (100 / (1 + Money_Flow_Ratio))

// Calculate MFI high and low bands
MFI_High = MFI - 80
MFI_Low = MFI - 20

// Plot the MFI
plot(MFI, color=color.blue, title="MFI")

// Plot the MFI high and low bands
hline(80, "MFI High", color=color.red, linestyle=hline.style_dashed)
hline(20, "MFI Low", color=color.green, linestyle=hline.style_dashed)
plot(MFI_High, color=color.red, title="MFI High Band")
plot(MFI_Low, color=color.green, title="MFI Low Band")

// EXPLANATION OF THE STRATEGY
//The provided Pine Script implements a trading strategy that includes stop loss (SL) and multiple take profit (TP) levels,
//with an option to activate a trailing stop at the third TP level. Here's a detailed breakdown of its components and functionality:

//Variables Initialization:
var float stop = na
var float limit1 = na
var float limit2 = na

// Converts a percentage to points based on the average position price and the minimum tick size.
percent2points(percent) =>
    strategy.position_avg_price * percent / 100 / syminfo.mintick

// Stop Loss and Take Profit Inputs:
//Defines inputs for stop loss and three take profit levels in percentage terms.
sl = percent2points(input(2.92, title="stop loss %%"))
tp1 = percent2points(input(1.12, title="take profit 1 %%"))
tp2 = percent2points(input(2.31, title="take profit 2 %%"))
tp3 = percent2points(input(3.91, title="take profit 3 %%"))
activateTrailingOnThirdStep = input(false,title="activate trailing on third stage (tp3 is amount, tp2 is offset level)")
log.info("Stop Loss (sl):", sl," Take Profit 1 (tp1):", tp1, " Take Profit 2 (tp2):", tp2," Take Profit 3 (tp3):", tp3)

// Current Profit Calculation:
//Calculates the current profit in points based on the position size and price.
curProfitInPts() =>
    if strategy.position_size > 0
        (high - strategy.position_avg_price) / syminfo.mintick
    else if strategy.position_size < 0
        (strategy.position_avg_price - low) / syminfo.mintick
    else
        0
// Stop Loss and Profit Target Price Calculations:
//Determines the stop loss and profit target prices based on the position size and offset points.
calcStopLossPrice(OffsetPts) =>
    if strategy.position_size > 0
        strategy.position_avg_price - OffsetPts * syminfo.mintick
    else if strategy.position_size < 0
        strategy.position_avg_price + OffsetPts * syminfo.mintick
    else
        0
calcProfitTrgtPrice(OffsetPts) =>
    calcStopLossPrice(-OffsetPts)
// Current Stage Determination:
//Determines the current stage of the trade based on the profit points reached.
getCurrentStage() =>
    var stage = 0
    if strategy.position_size == 0
        stage := 0
    if stage == 0 and strategy.position_size != 0
        stage := 1
    else if stage == 1 and curProfitInPts() >= tp1
        stage := 2
    else if stage == 2 and curProfitInPts() >= tp2
        stage := 3
    stage
stopLevel = -1.
profitLevel = calcProfitTrgtPrice(tp3)

log.info("Stop Level:", stopLevel)
log.info("Profit Level:", profitLevel)
//This part of the strategy sets up exit conditions based on the current stage of the trade and uses the same exit ID "x" to modify the exit parameters dynamically.
//The exit parameters include stop loss, take profit, and comments for each stage.
// based on current stage set up exit
// note: we use same exit ids ("x") consciously, for MODIFY the exit's parameters
curStage = getCurrentStage()
float op_operation = decision_tree_0_MSFT_30Min_6c8d8263(Short_MA, Long_MA, Short_Long_Diff, MA_Cross, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

log.info("Decision Tree Operation (op_operation):", op_operation)
if (op_operation <= 0)
    if curStage == 1
        stopLevel := calcStopLossPrice(sl)
        strategy.exit("x", loss = sl, profit = tp3, comment = "sl or tp3")
    else if curStage == 2
        stopLevel := calcStopLossPrice(0)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "breakeven or tp3")
    else if curStage == 3
        stopLevel := calcStopLossPrice(-tp1)
        strategy.exit("x", stop = stopLevel, profit = tp3, comment = "tp1 or tp3")
    else
        strategy.cancel("x")


//SIGNAL MANAGE    User Adjustments and Risk Management
// The user can adjust the threshold values for op_operation to control the level of risk they are willing to take:
// Lower op_operation Threshold for Buy Signal (e.g., 0.5 instead of 0.55):
//     Effect: Generates more buy signals, increasing the frequency of trades. This is suitable for a user willing to take more risks and potentially capture more trading opportunities.
// Higher op_operation Threshold for Buy Signal (e.g., 0.8 instead of 0.55):
//     Effect: Generates fewer buy signals, reducing the frequency of trades. This is suitable for a user seeking to take fewer risks and only enter trades under more favorable conditions.
// Lower op_operation Threshold for Signal Closure (e.g., -0.8 instead of -0.9):
//     Effect: Closes positions less frequently, allowing trades more room to recover from temporary unfavorable conditions. This increases risk but can capture larger gains if the market reverses favorably.
// Higher op_operation Threshold for Signal Closure (e.g., -0.95 instead of -0.9):
//     Effect: Closes positions more frequently, exiting trades quickly at the first sign of unfavorable conditions. This decreases risk but may result in missed opportunities for recovery.
//Signal BUY
FIXED_DOLLAR_AMOUNT  = 10000
positionSize = FIXED_DOLLAR_AMOUNT / close
log.info("Position Size (in dollars $",FIXED_DOLLAR_AMOUNT,"):", positionSize)

if (op_operation >= 0.55)
    stop := close * 0.965
    limit1 := close * 1.03
    limit2 := close * 1.02
    strategy.entry("x", strategy.long, qty=positionSize, stop=stop, comment="in")
//Signal SELL
if (op_operation <= -0.9)
    strategy.close("x", comment = "under Le1")

// Impact on the Dataset
//Stop Loss (SL): Limits the maximum loss by exiting the position if the price moves against the trade by a specified percentage.
//Take Profit (TP1, TP2, TP3): Defines profit-taking levels to secure gains at different stages.
//Trailing Stop: Optionally activates a trailing stop at the third TP level to lock in profits while allowing for further gains if the price continues to move favorably.
//Position Entry and Exit: The strategy's buy and sell signals determine when to enter and exit positions, influencing the dataset by marking the points of trade execution and closure.
//Current Stage Tracking: Monitors the trade's progress through predefined stages, adjusting stop and profit levels accordingly.
//This strategy is designed to manage risk and maximize profits through a structured approach, incorporating multiple exit levels and dynamic adjustments based on market conditions. The dataset will reflect these actions, showing entries, exits, stop loss activations, and profit-taking events, providing valuable information for backtesting and performance analysis.
//Random forest AI offers significant advantages in trading, including the ability to handle large data sets, reduce overfitting and provide more robust predictions through the aggregation of multiple decision trees.

// NOTE: While the Tuisku team stands behind the quality and effectiveness of this trading strategy,
// PLEASE be aware that there is NO GUARANTEE of specific results or profits. TRADING INVOLVES SIGNIFICANT RISK, and it is important to use this strategy with careful consideration of your financial situation and risk tolerance.
// For further information and support, please contact us at Tuisku.eu.



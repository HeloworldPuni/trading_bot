//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Chaikin_Money_Flow, L_Money_Flow_Index
// ID_model: MSFT_1Min_2CM0_de4dc763 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_MSFT_1Min_2CM0_de4dc763", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_MSFT_1Min_de4dc763(mf, ad_mf, ad, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( MFI <= 79.7812 )
		if( Raw_Money_Flow <= 329256 )
			if( Positive_Money_Flow <= 43814.2 )
				if( mf <= -0.113152 )
					if( ad <= 325 )
						if( Typical_Price <= 419.694 )
							if( MFI_High <= -21.5347 )
								if( MFI <= 55.1519 )
									ret := 0.290607
								if( MFI > 55.1519 )
									ret := 0.718750 // buy
							if( MFI_High > -21.5347 )
								if( mf <= -0.230572 )
									ret := 0.464912
								if( mf > -0.230572 )
									ret := -0.117117
						if( Typical_Price > 419.694 )
							if( Raw_Money_Flow <= 307043 )
								if( Money_Flow_Ratio <= 0.337053 )
									ret := 0.327465
								if( Money_Flow_Ratio > 0.337053 )
									ret := 0.158933
							if( Raw_Money_Flow > 307043 )
								if( MFI <= 42.3718 )
									ret := 0.195122
								if( MFI > 42.3718 )
									ret := -0.727273 // sell
					if( ad > 325 )
						if( Negative_Money_Flow <= 229091 )
							if( Negative_Money_Flow <= 213496 )
								if( ad <= 408.714 )
									ret := 0.416667
								if( ad > 408.714 )
									ret := -0.142857
							if( Negative_Money_Flow > 213496 )
								ret := 0.875000 // buy
						if( Negative_Money_Flow > 229091 )
							if( Negative_Money_Flow <= 243000 )
								ret := -0.818182 // sell
							if( Negative_Money_Flow > 243000 )
								if( Negative_Money_Flow <= 272852 )
									ret := 0.333333
								if( Negative_Money_Flow > 272852 )
									ret := -0.216216
				if( mf > -0.113152 )
					if( Typical_Price <= 399.99 )
						if( MFI <= 55.6047 )
							if( Money_Flow_Ratio <= 0.771904 )
								if( Typical_Price <= 395.965 )
									ret := 0.722222 // buy
								if( Typical_Price > 395.965 )
									ret := 0.250000
							if( Money_Flow_Ratio > 0.771904 )
								if( ad_mf <= -0.055186 )
									ret := 0.173913
								if( ad_mf > -0.055186 )
									ret := -0.666667
						if( MFI > 55.6047 )
							if( Raw_Money_Flow <= 199318 )
								if( Negative_Money_Flow_Sum <= 1.16705e+06 )
									ret := 0.100000
								if( Negative_Money_Flow_Sum > 1.16705e+06 )
									ret := 0.642857
							if( Raw_Money_Flow > 199318 )
								if( ad_mf <= -0.63082 )
									ret := 1.000000 // buy
								if( ad_mf > -0.63082 )
									ret := 0.739130 // buy
					if( Typical_Price > 399.99 )
						if( ad_mf <= 0.087264 )
							if( MFI_Low <= 34.7432 )
								if( Money_Flow_Ratio <= 1.14712 )
									ret := 0.107934
								if( Money_Flow_Ratio > 1.14712 )
									ret := 0.484076
							if( MFI_Low > 34.7432 )
								if( mf <= -0.003251 )
									ret := -0.134557
								if( mf > -0.003251 )
									ret := 0.099141
						if( ad_mf > 0.087264 )
							if( Raw_Money_Flow <= 303595 )
								if( MFI <= 34.7899 )
									ret := 0.094444
								if( MFI > 34.7899 )
									ret := -0.184647
							if( Raw_Money_Flow > 303595 )
								if( MFI <= 44.4154 )
									ret := 0.400000
								if( MFI > 44.4154 )
									ret := 0.615385
			if( Positive_Money_Flow > 43814.2 )
				if( MFI_Low <= -10.2732 )
					if( MFI_Low <= -15.6236 )
						if( Positive_Money_Flow <= 84855.7 )
							if( Positive_Money_Flow <= 68749.6 )
								ret := -0.133333
							if( Positive_Money_Flow > 68749.6 )
								ret := -0.615385
						if( Positive_Money_Flow > 84855.7 )
							if( Typical_Price <= 399.406 )
								ret := -0.583333
							if( Typical_Price > 399.406 )
								if( Positive_Money_Flow_Sum <= 3.82963e+06 )
									ret := -0.084034
								if( Positive_Money_Flow_Sum > 3.82963e+06 )
									ret := 0.384615
					if( MFI_Low > -15.6236 )
						if( Negative_Money_Flow_Sum <= 1.00826e+07 )
							ret := 0.300000
						if( Negative_Money_Flow_Sum > 1.00826e+07 )
							if( ad_mf <= 22.8906 )
								if( Negative_Money_Flow_Sum <= 1.13191e+07 )
									ret := -0.826087 // sell
								if( Negative_Money_Flow_Sum > 1.13191e+07 )
									ret := -0.293103
							if( ad_mf > 22.8906 )
								if( Money_Flow_Ratio <= 0.079013 )
									ret := -0.941176 // sell
								if( Money_Flow_Ratio > 0.079013 )
									ret := -0.600000
				if( MFI_Low > -10.2732 )
					if( MFI_Low <= -2.73387 )
						if( Positive_Money_Flow <= 117574 )
							if( MFI_High <= -68.3735 )
								ret := -0.230769
							if( MFI_High > -68.3735 )
								if( ad_mf <= -0.228466 )
									ret := -0.200000
								if( ad_mf > -0.228466 )
									ret := 0.694118
						if( Positive_Money_Flow > 117574 )
							if( Typical_Price <= 428.341 )
								if( Negative_Money_Flow_Sum <= 1.77287e+07 )
									ret := -0.047619
								if( Negative_Money_Flow_Sum > 1.77287e+07 )
									ret := -0.578947
							if( Typical_Price > 428.341 )
								if( Negative_Money_Flow_Sum <= 9.89865e+06 )
									ret := 0.602740
								if( Negative_Money_Flow_Sum > 9.89865e+06 )
									ret := -0.166667
					if( MFI_Low > -2.73387 )
						if( Negative_Money_Flow_Sum <= 4.636e+06 )
							if( Raw_Money_Flow <= 76732.4 )
								if( MFI <= 76.8968 )
									ret := -0.159389
								if( MFI > 76.8968 )
									ret := 0.666667
							if( Raw_Money_Flow > 76732.4 )
								if( Money_Flow_Ratio <= 0.696462 )
									ret := 0.167939
								if( Money_Flow_Ratio > 0.696462 )
									ret := 0.024635
						if( Negative_Money_Flow_Sum > 4.636e+06 )
							if( MFI_High <= -32.4349 )
								if( MFI <= 29.9638 )
									ret := -0.096606
								if( MFI > 29.9638 )
									ret := -0.328685
							if( MFI_High > -32.4349 )
								if( mf <= -0.122611 )
									ret := 0.333333
								if( mf > -0.122611 )
									ret := -0.178295
		if( Raw_Money_Flow > 329256 )
			if( Typical_Price <= 397.576 )
				if( Positive_Money_Flow_Sum <= 7.04069e+07 )
					if( Negative_Money_Flow_Sum <= 4.14481e+06 )
						if( ad_mf <= -30.3281 )
							if( MFI_High <= -47.6208 )
								ret := 0.100000
							if( MFI_High > -47.6208 )
								if( Typical_Price <= 391.685 )
									ret := 0.500000
								if( Typical_Price > 391.685 )
									ret := 0.914894 // buy
						if( ad_mf > -30.3281 )
							if( Typical_Price <= 392.906 )
								if( Positive_Money_Flow_Sum <= 3.73767e+06 )
									ret := -0.666667
								if( Positive_Money_Flow_Sum > 3.73767e+06 )
									ret := 0.083333
							if( Typical_Price > 392.906 )
								if( Negative_Money_Flow <= 524615 )
									ret := 0.733333 // buy
								if( Negative_Money_Flow > 524615 )
									ret := -0.416667
					if( Negative_Money_Flow_Sum > 4.14481e+06 )
						if( Typical_Price <= 386.712 )
							if( Positive_Money_Flow_Sum <= 1.56182e+07 )
								if( Typical_Price <= 384.838 )
									ret := 0.800000 // buy
								if( Typical_Price > 384.838 )
									ret := -0.875000 // sell
							if( Positive_Money_Flow_Sum > 1.56182e+07 )
								ret := 1.000000 // buy
						if( Typical_Price > 386.712 )
							if( Positive_Money_Flow_Sum <= 4.49023e+06 )
								if( MFI_High <= -41.2796 )
									ret := 0.100671
								if( MFI_High > -41.2796 )
									ret := 0.846154 // buy
							if( Positive_Money_Flow_Sum > 4.49023e+06 )
								if( MFI_Low <= -9.12043 )
									ret := 0.857143 // buy
								if( MFI_Low > -9.12043 )
									ret := -0.111364
				if( Positive_Money_Flow_Sum > 7.04069e+07 )
					if( ad <= 191711 )
						if( mf <= 0.137489 )
							if( Positive_Money_Flow_Sum <= 2.033e+08 )
								if( MFI_Low <= -1.92582 )
									ret := -0.370370
								if( MFI_Low > -1.92582 )
									ret := 0.183976
							if( Positive_Money_Flow_Sum > 2.033e+08 )
								if( ad <= 47306 )
									ret := 0.769231 // buy
								if( ad > 47306 )
									ret := 0.311111
						if( mf > 0.137489 )
							if( Positive_Money_Flow <= 3.37643e+07 )
								if( Positive_Money_Flow_Sum <= 2.43672e+08 )
									ret := 0.211538
								if( Positive_Money_Flow_Sum > 2.43672e+08 )
									ret := -0.540000
							if( Positive_Money_Flow > 3.37643e+07 )
								ret := -0.736842 // sell
					if( ad > 191711 )
						if( mf <= -0.051792 )
							ret := 0.142857
						if( mf > -0.051792 )
							if( MFI_High <= -14.8467 )
								ret := -1.000000 // sell
							if( MFI_High > -14.8467 )
								ret := -0.800000 // sell
			if( Typical_Price > 397.576 )
				if( Money_Flow_Ratio <= 0.010501 )
					if( Negative_Money_Flow <= 1.54645e+07 )
						if( Positive_Money_Flow <= 347149 )
							if( Positive_Money_Flow_Sum <= 1.17942e+06 )
								if( Positive_Money_Flow_Sum <= 867087 )
									ret := -0.153846
								if( Positive_Money_Flow_Sum > 867087 )
									ret := -0.600000
							if( Positive_Money_Flow_Sum > 1.17942e+06 )
								if( ad_mf <= -273.72 )
									ret := 0.850000 // buy
								if( ad_mf > -273.72 )
									ret := 0.187500
						if( Positive_Money_Flow > 347149 )
							if( Positive_Money_Flow_Sum <= 1.84505e+06 )
								if( Positive_Money_Flow <= 511203 )
									ret := -0.600000
								if( Positive_Money_Flow > 511203 )
									ret := -1.000000 // sell
							if( Positive_Money_Flow_Sum > 1.84505e+06 )
								ret := -0.500000
					if( Negative_Money_Flow > 1.54645e+07 )
						if( Negative_Money_Flow_Sum <= 1.75919e+08 )
							ret := -0.100000
						if( Negative_Money_Flow_Sum > 1.75919e+08 )
							if( Raw_Money_Flow <= 1.76517e+08 )
								if( Typical_Price <= 415.518 )
									ret := -0.350000
								if( Typical_Price > 415.518 )
									ret := -0.905405 // sell
							if( Raw_Money_Flow > 1.76517e+08 )
								ret := -0.312500
				if( Money_Flow_Ratio > 0.010501 )
					if( mf <= 0.320745 )
						if( ad <= -38.3912 )
							if( Negative_Money_Flow_Sum <= 1.5323e+07 )
								if( Typical_Price <= 453.265 )
									ret := 0.184440
								if( Typical_Price > 453.265 )
									ret := -0.269036
							if( Negative_Money_Flow_Sum > 1.5323e+07 )
								if( Negative_Money_Flow <= 4.13209e+07 )
									ret := 0.002004
								if( Negative_Money_Flow > 4.13209e+07 )
									ret := 0.157628
						if( ad > -38.3912 )
							if( Positive_Money_Flow <= 5.89463e+06 )
								if( Positive_Money_Flow_Sum <= 3.04844e+07 )
									ret := -0.102047
								if( Positive_Money_Flow_Sum > 3.04844e+07 )
									ret := -0.019378
							if( Positive_Money_Flow > 5.89463e+06 )
								if( Positive_Money_Flow_Sum <= 1.94541e+08 )
									ret := 0.014932
								if( Positive_Money_Flow_Sum > 1.94541e+08 )
									ret := -0.122849
					if( mf > 0.320745 )
						if( Negative_Money_Flow_Sum <= 1.42618e+07 )
							if( ad <= 7.11333 )
								if( Money_Flow_Ratio <= 3.75168 )
									ret := -0.138196
								if( Money_Flow_Ratio > 3.75168 )
									ret := 0.894737 // buy
							if( ad > 7.11333 )
								if( Raw_Money_Flow <= 1.75283e+06 )
									ret := -0.286190
								if( Raw_Money_Flow > 1.75283e+06 )
									ret := -0.587940
						if( Negative_Money_Flow_Sum > 1.42618e+07 )
							if( MFI_High <= -75.8479 )
								if( Negative_Money_Flow_Sum <= 1.46153e+08 )
									ret := -0.129032
								if( Negative_Money_Flow_Sum > 1.46153e+08 )
									ret := -0.679245
							if( MFI_High > -75.8479 )
								if( Typical_Price <= 460.411 )
									ret := -0.028649
								if( Typical_Price > 460.411 )
									ret := 0.803279 // buy
	if( MFI > 79.7812 )
		if( Positive_Money_Flow_Sum <= 2.15241e+07 )
			if( Typical_Price <= 414.062 )
				if( ad_mf <= -0.640403 )
					if( Raw_Money_Flow <= 312282 )
						if( Negative_Money_Flow <= 7011.71 )
							ret := 0.312500
						if( Negative_Money_Flow > 7011.71 )
							if( ad <= -268.982 )
								ret := 0.444444
							if( ad > -268.982 )
								ret := 0.961538 // buy
					if( Raw_Money_Flow > 312282 )
						if( mf <= -0.115382 )
							if( mf <= -0.38803 )
								ret := 0.090909
							if( mf > -0.38803 )
								ret := 0.785714 // buy
						if( mf > -0.115382 )
							if( MFI <= 81.6839 )
								ret := 0.454545
							if( MFI > 81.6839 )
								if( mf <= 0.551687 )
									ret := -0.212766
								if( mf > 0.551687 )
									ret := -0.800000 // sell
				if( ad_mf > -0.640403 )
					if( Raw_Money_Flow <= 105153 )
						if( Negative_Money_Flow_Sum <= 503581 )
							if( Negative_Money_Flow <= 7334.49 )
								ret := 0.437500
							if( Negative_Money_Flow > 7334.49 )
								ret := 0.888889 // buy
						if( Negative_Money_Flow_Sum > 503581 )
							if( Negative_Money_Flow <= 12583.8 )
								ret := -0.133333
							if( Negative_Money_Flow > 12583.8 )
								ret := 0.333333
					if( Raw_Money_Flow > 105153 )
						if( MFI_Low <= 71.1505 )
							if( Positive_Money_Flow_Sum <= 2.11411e+06 )
								ret := 1.000000 // buy
							if( Positive_Money_Flow_Sum > 2.11411e+06 )
								if( Typical_Price <= 391.925 )
									ret := 0.615385
								if( Typical_Price > 391.925 )
									ret := -0.273349
						if( MFI_Low > 71.1505 )
							if( ad_mf <= 1538.54 )
								if( Positive_Money_Flow_Sum <= 1.17848e+07 )
									ret := 0.300000
								if( Positive_Money_Flow_Sum > 1.17848e+07 )
									ret := -0.562500
							if( ad_mf > 1538.54 )
								ret := 0.923077 // buy
			if( Typical_Price > 414.062 )
				if( ad_mf <= -0.497663 )
					if( MFI_High <= 0.106417 )
						if( Negative_Money_Flow <= 561650 )
							ret := -0.357143
						if( Negative_Money_Flow > 561650 )
							ret := -0.916667 // sell
					if( MFI_High > 0.106417 )
						if( MFI_Low <= 64.7466 )
							if( Raw_Money_Flow <= 3.89151e+06 )
								if( Positive_Money_Flow <= 2.79095e+06 )
									ret := 0.231707
								if( Positive_Money_Flow > 2.79095e+06 )
									ret := 0.947368 // buy
							if( Raw_Money_Flow > 3.89151e+06 )
								ret := -0.666667
						if( MFI_Low > 64.7466 )
							if( MFI_Low <= 65.8851 )
								if( mf <= 0.047355 )
									ret := -0.806452 // sell
								if( mf > 0.047355 )
									ret := 0.058824
							if( MFI_Low > 65.8851 )
								if( Money_Flow_Ratio <= 6.23535 )
									ret := 0.642857
								if( Money_Flow_Ratio > 6.23535 )
									ret := -0.055901
				if( ad_mf > -0.497663 )
					if( Positive_Money_Flow_Sum <= 5.33365e+06 )
						if( MFI <= 89.3123 )
							if( Money_Flow_Ratio <= 6.86889 )
								if( Raw_Money_Flow <= 374454 )
									ret := -0.302682
								if( Raw_Money_Flow > 374454 )
									ret := 0.060976
							if( Money_Flow_Ratio > 6.86889 )
								if( Typical_Price <= 416.313 )
									ret := 0.222222
								if( Typical_Price > 416.313 )
									ret := -0.684211
						if( MFI > 89.3123 )
							if( Negative_Money_Flow_Sum <= 347831 )
								if( Positive_Money_Flow <= 161849 )
									ret := 0.518519
								if( Positive_Money_Flow > 161849 )
									ret := 0.045455
							if( Negative_Money_Flow_Sum > 347831 )
								if( Typical_Price <= 427.243 )
									ret := 0.280000
								if( Typical_Price > 427.243 )
									ret := -0.714286 // sell
					if( Positive_Money_Flow_Sum > 5.33365e+06 )
						if( Raw_Money_Flow <= 3.45563e+06 )
							if( Negative_Money_Flow <= 16850.9 )
								if( Raw_Money_Flow <= 777560 )
									ret := -0.627907
								if( Raw_Money_Flow > 777560 )
									ret := -0.248175
							if( Negative_Money_Flow > 16850.9 )
								if( Negative_Money_Flow_Sum <= 2.50249e+06 )
									ret := -0.313187
								if( Negative_Money_Flow_Sum > 2.50249e+06 )
									ret := 0.255319
						if( Raw_Money_Flow > 3.45563e+06 )
							if( mf <= 0.382179 )
								if( Positive_Money_Flow <= 9.1833e+06 )
									ret := -1.000000 // sell
								if( Positive_Money_Flow > 9.1833e+06 )
									ret := -0.727273 // sell
							if( mf > 0.382179 )
								ret := -0.615385
		if( Positive_Money_Flow_Sum > 2.15241e+07 )
			if( Negative_Money_Flow_Sum <= 5.73344e+08 )
				if( Typical_Price <= 409.028 )
					if( Money_Flow_Ratio <= 16.5543 )
						if( mf <= 0.551784 )
							if( Raw_Money_Flow <= 7.83764e+06 )
								if( MFI_High <= 9.28769 )
									ret := 0.156250
								if( MFI_High > 9.28769 )
									ret := -0.287671
							if( Raw_Money_Flow > 7.83764e+06 )
								if( Negative_Money_Flow <= 1.97298e+07 )
									ret := -0.349057
								if( Negative_Money_Flow > 1.97298e+07 )
									ret := 0.071429
						if( mf > 0.551784 )
							if( Raw_Money_Flow <= 478944 )
								ret := 0.818182 // buy
							if( Raw_Money_Flow > 478944 )
								if( MFI <= 88.911 )
									ret := -0.762712 // sell
								if( MFI > 88.911 )
									ret := -0.040000
					if( Money_Flow_Ratio > 16.5543 )
						if( Raw_Money_Flow <= 1.52825e+06 )
							if( Positive_Money_Flow <= 212920 )
								if( MFI <= 96.5966 )
									ret := -0.958333 // sell
								if( MFI > 96.5966 )
									ret := -0.611111
							if( Positive_Money_Flow > 212920 )
								if( Money_Flow_Ratio <= 28.9676 )
									ret := 0.214286
								if( Money_Flow_Ratio > 28.9676 )
									ret := -0.619048
						if( Raw_Money_Flow > 1.52825e+06 )
							if( Positive_Money_Flow_Sum <= 1.79304e+08 )
								ret := -0.454545
							if( Positive_Money_Flow_Sum > 1.79304e+08 )
								if( MFI_High <= 16.1576 )
									ret := 0.555556
								if( MFI_High > 16.1576 )
									ret := 0.083333
				if( Typical_Price > 409.028 )
					if( Positive_Money_Flow_Sum <= 2.05164e+09 )
						if( Raw_Money_Flow <= 1.47269e+07 )
							if( Typical_Price <= 416.975 )
								if( Positive_Money_Flow <= 8.07204e+06 )
									ret := 0.232877
								if( Positive_Money_Flow > 8.07204e+06 )
									ret := -0.082305
							if( Typical_Price > 416.975 )
								if( Raw_Money_Flow <= 9.63366e+06 )
									ret := -0.014628
								if( Raw_Money_Flow > 9.63366e+06 )
									ret := -0.182692
						if( Raw_Money_Flow > 1.47269e+07 )
							if( MFI_Low <= 64.7291 )
								if( Positive_Money_Flow_Sum <= 4.41406e+08 )
									ret := 0.044444
								if( Positive_Money_Flow_Sum > 4.41406e+08 )
									ret := -0.525773
							if( MFI_Low > 64.7291 )
								if( Typical_Price <= 459.34 )
									ret := 0.195971
								if( Typical_Price > 459.34 )
									ret := 0.868421 // buy
					if( Positive_Money_Flow_Sum > 2.05164e+09 )
						if( MFI <= 99.0349 )
							if( Money_Flow_Ratio <= 10.3848 )
								if( Negative_Money_Flow <= 3.2471e+07 )
									ret := 0.132867
								if( Negative_Money_Flow > 3.2471e+07 )
									ret := -0.750000 // sell
							if( Money_Flow_Ratio > 10.3848 )
								if( MFI_Low <= 72.0893 )
									ret := -0.952381 // sell
								if( MFI_Low > 72.0893 )
									ret := -0.354331
						if( MFI > 99.0349 )
							ret := 0.769231 // buy
			if( Negative_Money_Flow_Sum > 5.73344e+08 )
				if( Positive_Money_Flow_Sum <= 3.57979e+09 )
					if( mf <= 0.055535 )
						ret := 0.777778 // buy
					if( mf > 0.055535 )
						ret := 1.000000 // buy
				if( Positive_Money_Flow_Sum > 3.57979e+09 )
					ret := 0.263158
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator L_Chaikin_Money_Flow 
 //@version=5
//indicator title="Chaikin Money Flow", shorttitle="CMF", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
var cumVol = 0.
cumVol += nz(volume)
if barstate.islast and cumVol == 0
    runtime.error("No volume is provided by the data vendor.")
length_CMF = input.int(20, minval=1)
ad = close==high and close==low or high==low ? 0 : ((2*close-low-high)/(high-low))*volume
mf = math.sum(ad, length_CMF) / math.sum(volume, length_CMF)
plot(mf, color=#43A047, title="MF")
hline(0, color=#787B86, title="Zero", linestyle=hline.style_dashed)


ad_mf = ad - mf

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
float op_operation = decision_tree_0_MSFT_1Min_de4dc763(mf, ad_mf, ad, Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price)

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



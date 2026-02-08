//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: L_Money_Flow_Index, L_Stochastic_RSI
// ID_model: GME_15Min_2MS0_60738b27 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_GME_15Min_2MS0_60738b27", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_GME_15Min_60738b27(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, d, d_k, smoothK_k, k, rsi1, smoothD_d)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( k <= 64.4324 )
		if( Typical_Price <= 12.6753 )
			if( Money_Flow_Ratio <= 0.395776 )
				if( smoothK_k <= 25.974 )
					if( MFI_High <= -79.0744 )
						if( Negative_Money_Flow <= 1.04494e+06 )
							if( smoothK_k <= 15.6512 )
								if( k <= 5.0515 )
									ret := -0.048780
								if( k > 5.0515 )
									ret := 0.625000
							if( smoothK_k > 15.6512 )
								if( Typical_Price <= 4.20823 )
									ret := -1.000000 // sell
								if( Typical_Price > 4.20823 )
									ret := -0.066667
						if( Negative_Money_Flow > 1.04494e+06 )
							if( Negative_Money_Flow_Sum <= 1.93539e+07 )
								if( Negative_Money_Flow <= 1.23204e+06 )
									ret := 1.000000 // buy
								if( Negative_Money_Flow > 1.23204e+06 )
									ret := 0.385965
							if( Negative_Money_Flow_Sum > 1.93539e+07 )
								ret := 1.000000 // buy
					if( MFI_High > -79.0744 )
						if( d_k <= -1.7803 )
							if( smoothK_k <= 25.6766 )
								if( Positive_Money_Flow_Sum <= 1.15404e+06 )
									ret := 0.352000
								if( Positive_Money_Flow_Sum > 1.15404e+06 )
									ret := 0.084567
							if( smoothK_k > 25.6766 )
								ret := 1.000000 // buy
						if( d_k > -1.7803 )
							if( rsi1 <= 17.3532 )
								if( MFI_Low <= -5.04056 )
									ret := 0.369942
								if( MFI_Low > -5.04056 )
									ret := -0.077778
							if( rsi1 > 17.3532 )
								if( Typical_Price <= 4.11583 )
									ret := 0.225806
								if( Typical_Price > 4.11583 )
									ret := -0.061801
				if( smoothK_k > 25.974 )
					if( rsi1 <= 56.7711 )
						if( Raw_Money_Flow <= 1.20315e+07 )
							if( d <= 40.6193 )
								if( Money_Flow_Ratio <= 0.242637 )
									ret := -0.346247
								if( Money_Flow_Ratio > 0.242637 )
									ret := 0.064000
							if( d > 40.6193 )
								if( Typical_Price <= 4.21718 )
									ret := 0.315508
								if( Typical_Price > 4.21718 )
									ret := -0.056110
						if( Raw_Money_Flow > 1.20315e+07 )
							ret := 0.789474 // buy
					if( rsi1 > 56.7711 )
						if( d <= 61.7141 )
							if( Negative_Money_Flow_Sum <= 7.33913e+06 )
								if( d <= 40.8432 )
									ret := 0.312500
								if( d > 40.8432 )
									ret := -1.000000 // sell
							if( Negative_Money_Flow_Sum > 7.33913e+06 )
								if( MFI_High <= -61.5311 )
									ret := -0.653846
								if( MFI_High > -61.5311 )
									ret := -0.957447 // sell
						if( d > 61.7141 )
							ret := 0.062500
			if( Money_Flow_Ratio > 0.395776 )
				if( Positive_Money_Flow_Sum <= 796754 )
					if( Negative_Money_Flow_Sum <= 116749 )
						if( smoothK_k <= 21.3838 )
							if( rsi1 <= 58.2128 )
								if( Typical_Price <= 10.8166 )
									ret := 0.862500 // buy
								if( Typical_Price > 10.8166 )
									ret := 0.393939
							if( rsi1 > 58.2128 )
								ret := -0.400000
						if( smoothK_k > 21.3838 )
							if( Negative_Money_Flow_Sum <= 112438 )
								if( Raw_Money_Flow <= 16844.3 )
									ret := -0.227488
								if( Raw_Money_Flow > 16844.3 )
									ret := 0.198630
							if( Negative_Money_Flow_Sum > 112438 )
								ret := 0.700000 // buy
					if( Negative_Money_Flow_Sum > 116749 )
						if( smoothK_k <= 14.1027 )
							if( Negative_Money_Flow_Sum <= 139804 )
								ret := -0.833333 // sell
							if( Negative_Money_Flow_Sum > 139804 )
								if( rsi1 <= 45.6133 )
									ret := 0.411111
								if( rsi1 > 45.6133 )
									ret := -0.135135
						if( smoothK_k > 14.1027 )
							if( d_k <= -0.222887 )
								if( rsi1 <= 49.3603 )
									ret := 0.343750
								if( rsi1 > 49.3603 )
									ret := -0.309735
							if( d_k > -0.222887 )
								if( smoothD_d <= 48.8023 )
									ret := -0.625000
								if( smoothD_d > 48.8023 )
									ret := -0.122137
				if( Positive_Money_Flow_Sum > 796754 )
					if( Positive_Money_Flow_Sum <= 3.32973e+07 )
						if( Money_Flow_Ratio <= 0.950304 )
							if( Typical_Price <= 5.50224 )
								if( Raw_Money_Flow <= 77557.2 )
									ret := 0.478191
								if( Raw_Money_Flow > 77557.2 )
									ret := 0.207330
							if( Typical_Price > 5.50224 )
								if( Negative_Money_Flow <= 2.69952e+06 )
									ret := 0.093328
								if( Negative_Money_Flow > 2.69952e+06 )
									ret := 0.636364
						if( Money_Flow_Ratio > 0.950304 )
							if( Positive_Money_Flow <= 305.7 )
								if( Negative_Money_Flow <= 937655 )
									ret := 0.240705
								if( Negative_Money_Flow > 937655 )
									ret := 0.065598
							if( Positive_Money_Flow > 305.7 )
								if( Money_Flow_Ratio <= 1.95391 )
									ret := -0.056724
								if( Money_Flow_Ratio > 1.95391 )
									ret := 0.148294
					if( Positive_Money_Flow_Sum > 3.32973e+07 )
						if( MFI <= 42.1175 )
							ret := -0.384615
						if( MFI > 42.1175 )
							if( k <= 12.3088 )
								if( MFI <= 78.7574 )
									ret := -0.173913
								if( MFI > 78.7574 )
									ret := 0.750000 // buy
							if( k > 12.3088 )
								if( Raw_Money_Flow <= 3.78768e+06 )
									ret := 0.811966 // buy
								if( Raw_Money_Flow > 3.78768e+06 )
									ret := 0.400000
		if( Typical_Price > 12.6753 )
			if( Negative_Money_Flow_Sum <= 126789 )
				if( Positive_Money_Flow_Sum <= 275130 )
					if( d <= 10.7625 )
						if( rsi1 <= 37.8814 )
							if( Positive_Money_Flow_Sum <= 159044 )
								ret := 0.000000
							if( Positive_Money_Flow_Sum > 159044 )
								ret := 0.571429
						if( rsi1 > 37.8814 )
							if( rsi1 <= 49.6071 )
								ret := 0.000000
							if( rsi1 > 49.6071 )
								ret := -0.181818
					if( d > 10.7625 )
						if( MFI <= 48.3607 )
							if( Positive_Money_Flow_Sum <= 41209.1 )
								if( Negative_Money_Flow <= 3885.67 )
									ret := -0.090909
								if( Negative_Money_Flow > 3885.67 )
									ret := -0.947368 // sell
							if( Positive_Money_Flow_Sum > 41209.1 )
								if( smoothD_d <= 39.2172 )
									ret := -0.295775
								if( smoothD_d > 39.2172 )
									ret := 0.338462
						if( MFI > 48.3607 )
							if( Positive_Money_Flow <= 8212.4 )
								if( Typical_Price <= 17.7442 )
									ret := -0.362319
								if( Typical_Price > 17.7442 )
									ret := 0.060345
							if( Positive_Money_Flow > 8212.4 )
								if( Raw_Money_Flow <= 64604.2 )
									ret := -0.627119
								if( Raw_Money_Flow > 64604.2 )
									ret := -0.047619
				if( Positive_Money_Flow_Sum > 275130 )
					if( d <= 43.2622 )
						if( Positive_Money_Flow_Sum <= 1.80582e+06 )
							if( smoothD_d <= 30.0439 )
								if( k <= 12.4781 )
									ret := 0.100000
								if( k > 12.4781 )
									ret := 0.777778 // buy
							if( smoothD_d > 30.0439 )
								ret := 0.192308
						if( Positive_Money_Flow_Sum > 1.80582e+06 )
							if( d_k <= -11.1029 )
								ret := -0.714286 // sell
							if( d_k > -11.1029 )
								if( d <= 30.9775 )
									ret := -0.035714
								if( d > 30.9775 )
									ret := 0.500000
					if( d > 43.2622 )
						if( Money_Flow_Ratio <= 3.83274 )
							ret := -0.937500 // sell
						if( Money_Flow_Ratio > 3.83274 )
							if( Positive_Money_Flow_Sum <= 361678 )
								ret := 0.444444
							if( Positive_Money_Flow_Sum > 361678 )
								if( k <= 54.544 )
									ret := 0.090909
								if( k > 54.544 )
									ret := -0.583333
			if( Negative_Money_Flow_Sum > 126789 )
				if( Negative_Money_Flow <= 3.37614 )
					if( Negative_Money_Flow_Sum <= 1.34497e+07 )
						if( rsi1 <= 37.9916 )
							if( MFI_High <= -16.6022 )
								if( Positive_Money_Flow_Sum <= 4.1924e+06 )
									ret := 0.034113
								if( Positive_Money_Flow_Sum > 4.1924e+06 )
									ret := -0.130199
							if( MFI_High > -16.6022 )
								if( rsi1 <= 36.6463 )
									ret := 0.244275
								if( rsi1 > 36.6463 )
									ret := 0.608696
						if( rsi1 > 37.9916 )
							if( MFI_Low <= 26.7166 )
								if( k <= 30.8387 )
									ret := -0.097789
								if( k > 30.8387 )
									ret := -0.296273
							if( MFI_Low > 26.7166 )
								if( Positive_Money_Flow <= 2.67667e+06 )
									ret := -0.039015
								if( Positive_Money_Flow > 2.67667e+06 )
									ret := -0.183417
					if( Negative_Money_Flow_Sum > 1.34497e+07 )
						if( smoothD_d <= 8.90498 )
							if( MFI <= 54.2251 )
								if( smoothD_d <= -0.151849 )
									ret := -0.012759
								if( smoothD_d > -0.151849 )
									ret := -0.135426
							if( MFI > 54.2251 )
								if( Positive_Money_Flow_Sum <= 5.33231e+07 )
									ret := 0.313333
								if( Positive_Money_Flow_Sum > 5.33231e+07 )
									ret := 0.006135
						if( smoothD_d > 8.90498 )
							if( Negative_Money_Flow_Sum <= 2.03114e+09 )
								if( Positive_Money_Flow_Sum <= 3.85293e+07 )
									ret := -0.010872
								if( Positive_Money_Flow_Sum > 3.85293e+07 )
									ret := 0.103620
							if( Negative_Money_Flow_Sum > 2.03114e+09 )
								if( Money_Flow_Ratio <= 0.499663 )
									ret := 0.500000
								if( Money_Flow_Ratio > 0.499663 )
									ret := -0.506944
				if( Negative_Money_Flow > 3.37614 )
					if( Raw_Money_Flow <= 63108.6 )
						if( MFI <= 57.5308 )
							if( Typical_Price <= 17.3702 )
								if( MFI_High <= -36.5312 )
									ret := 0.381770
								if( MFI_High > -36.5312 )
									ret := 0.060748
							if( Typical_Price > 17.3702 )
								if( MFI <= 46.5287 )
									ret := 0.115063
								if( MFI > 46.5287 )
									ret := 0.295585
						if( MFI > 57.5308 )
							if( rsi1 <= 52.6839 )
								if( MFI <= 83.6329 )
									ret := 0.083955
								if( MFI > 83.6329 )
									ret := 0.664430
							if( rsi1 > 52.6839 )
								if( Raw_Money_Flow <= 30461.2 )
									ret := -0.217277
								if( Raw_Money_Flow > 30461.2 )
									ret := 0.109589
					if( Raw_Money_Flow > 63108.6 )
						if( Positive_Money_Flow_Sum <= 1.02634e+09 )
							if( MFI_Low <= 56.0427 )
								if( Negative_Money_Flow_Sum <= 3.20266e+09 )
									ret := 0.007424
								if( Negative_Money_Flow_Sum > 3.20266e+09 )
									ret := -0.760563 // sell
							if( MFI_Low > 56.0427 )
								if( Positive_Money_Flow_Sum <= 2.17286e+08 )
									ret := 0.319899
								if( Positive_Money_Flow_Sum > 2.17286e+08 )
									ret := -0.030075
						if( Positive_Money_Flow_Sum > 1.02634e+09 )
							if( Typical_Price <= 239.536 )
								if( k <= 34.7968 )
									ret := 0.566745
								if( k > 34.7968 )
									ret := 0.208571
							if( Typical_Price > 239.536 )
								if( Money_Flow_Ratio <= 1.60807 )
									ret := 0.264151
								if( Money_Flow_Ratio > 1.60807 )
									ret := -0.449541
	if( k > 64.4324 )
		if( Positive_Money_Flow_Sum <= 1.33552e+08 )
			if( Negative_Money_Flow <= 42.1978 )
				if( rsi1 <= 65.3874 )
					if( rsi1 <= 50.7307 )
						if( rsi1 <= 45.9833 )
							if( rsi1 <= 39.6019 )
								if( Positive_Money_Flow_Sum <= 5.05139e+07 )
									ret := 0.108541
								if( Positive_Money_Flow_Sum > 5.05139e+07 )
									ret := -0.388889
							if( rsi1 > 39.6019 )
								if( Money_Flow_Ratio <= 0.463572 )
									ret := -0.314935
								if( Money_Flow_Ratio > 0.463572 )
									ret := -0.036488
						if( rsi1 > 45.9833 )
							if( Raw_Money_Flow <= 1.68494e+06 )
								if( Positive_Money_Flow_Sum <= 188003 )
									ret := -0.236559
								if( Positive_Money_Flow_Sum > 188003 )
									ret := 0.009514
							if( Raw_Money_Flow > 1.68494e+06 )
								if( Positive_Money_Flow_Sum <= 1.54759e+07 )
									ret := -0.040816
								if( Positive_Money_Flow_Sum > 1.54759e+07 )
									ret := 0.335505
					if( rsi1 > 50.7307 )
						if( Money_Flow_Ratio <= 0.857205 )
							if( d <= 79.8697 )
								if( MFI <= 32.6634 )
									ret := -0.111111
								if( MFI > 32.6634 )
									ret := -0.321818
							if( d > 79.8697 )
								if( MFI_Low <= -14.1364 )
									ret := -0.580645
								if( MFI_Low > -14.1364 )
									ret := -0.097884
						if( Money_Flow_Ratio > 0.857205 )
							if( Typical_Price <= 23.5512 )
								if( d_k <= 0.909193 )
									ret := -0.057152
								if( d_k > 0.909193 )
									ret := 0.084163
							if( Typical_Price > 23.5512 )
								if( MFI <= 98.4326 )
									ret := -0.149460
								if( MFI > 98.4326 )
									ret := 0.512195
				if( rsi1 > 65.3874 )
					if( MFI_Low <= 32.0561 )
						if( Negative_Money_Flow_Sum <= 1.15273e+07 )
							if( k <= 89.2359 )
								if( Raw_Money_Flow <= 1.11821e+06 )
									ret := -0.604167
								if( Raw_Money_Flow > 1.11821e+06 )
									ret := 0.176471
							if( k > 89.2359 )
								if( Raw_Money_Flow <= 74664.5 )
									ret := -0.464000
								if( Raw_Money_Flow > 74664.5 )
									ret := -0.040404
						if( Negative_Money_Flow_Sum > 1.15273e+07 )
							if( Positive_Money_Flow_Sum <= 4.14817e+07 )
								if( k <= 76.194 )
									ret := -0.437500
								if( k > 76.194 )
									ret := -0.089888
							if( Positive_Money_Flow_Sum > 4.14817e+07 )
								if( smoothD_d <= 88.7548 )
									ret := -0.380952
								if( smoothD_d > 88.7548 )
									ret := -0.789474 // sell
					if( MFI_Low > 32.0561 )
						if( Negative_Money_Flow_Sum <= 2.86335e+06 )
							if( Raw_Money_Flow <= 1.51824e+07 )
								if( Positive_Money_Flow_Sum <= 83570.6 )
									ret := 0.888889 // buy
								if( Positive_Money_Flow_Sum > 83570.6 )
									ret := -0.272468
							if( Raw_Money_Flow > 1.51824e+07 )
								if( MFI_Low <= 78.0826 )
									ret := -0.243697
								if( MFI_Low > 78.0826 )
									ret := 0.465649
						if( Negative_Money_Flow_Sum > 2.86335e+06 )
							if( MFI_Low <= 55.848 )
								if( Negative_Money_Flow_Sum <= 8.41761e+06 )
									ret := -0.025385
								if( Negative_Money_Flow_Sum > 8.41761e+06 )
									ret := -0.236034
							if( MFI_Low > 55.848 )
								if( Positive_Money_Flow_Sum <= 3.44571e+07 )
									ret := -0.125270
								if( Positive_Money_Flow_Sum > 3.44571e+07 )
									ret := 0.149404
			if( Negative_Money_Flow > 42.1978 )
				if( Money_Flow_Ratio <= 420.612 )
					if( Negative_Money_Flow <= 228050 )
						if( d_k <= 6.29159 )
							if( Negative_Money_Flow <= 23225.6 )
								if( Negative_Money_Flow_Sum <= 1.62396e+06 )
									ret := -0.211661
								if( Negative_Money_Flow_Sum > 1.62396e+06 )
									ret := 0.075995
							if( Negative_Money_Flow > 23225.6 )
								if( Negative_Money_Flow_Sum <= 929189 )
									ret := -0.061692
								if( Negative_Money_Flow_Sum > 929189 )
									ret := 0.125345
						if( d_k > 6.29159 )
							if( Money_Flow_Ratio <= 54.3093 )
								if( Positive_Money_Flow_Sum <= 4.35208e+07 )
									ret := 0.209251
								if( Positive_Money_Flow_Sum > 4.35208e+07 )
									ret := -0.189189
							if( Money_Flow_Ratio > 54.3093 )
								if( MFI_High <= 18.6815 )
									ret := 0.916667 // buy
								if( MFI_High > 18.6815 )
									ret := 0.650000
					if( Negative_Money_Flow > 228050 )
						if( Negative_Money_Flow <= 2.91602e+06 )
							if( Negative_Money_Flow_Sum <= 2.18081e+07 )
								if( Positive_Money_Flow <= 426.741 )
									ret := -0.050306
								if( Positive_Money_Flow > 426.741 )
									ret := -0.337931
							if( Negative_Money_Flow_Sum > 2.18081e+07 )
								if( MFI_High <= -32.6805 )
									ret := 0.219262
								if( MFI_High > -32.6805 )
									ret := -0.050676
						if( Negative_Money_Flow > 2.91602e+06 )
							if( MFI_Low <= 9.40208 )
								if( MFI <= 3.69374 )
									ret := -0.764706 // sell
								if( MFI > 3.69374 )
									ret := 0.266094
							if( MFI_Low > 9.40208 )
								if( Raw_Money_Flow <= 1.1009e+07 )
									ret := -0.188204
								if( Raw_Money_Flow > 1.1009e+07 )
									ret := -0.010695
				if( Money_Flow_Ratio > 420.612 )
					ret := -1.000000 // sell
		if( Positive_Money_Flow_Sum > 1.33552e+08 )
			if( Positive_Money_Flow_Sum <= 3.56015e+08 )
				if( Raw_Money_Flow <= 4.6458e+07 )
					if( Typical_Price <= 132.517 )
						if( rsi1 <= 76.2935 )
							if( Negative_Money_Flow_Sum <= 7.50927e+07 )
								if( Raw_Money_Flow <= 3.5022e+06 )
									ret := -0.173077
								if( Raw_Money_Flow > 3.5022e+06 )
									ret := 0.336842
							if( Negative_Money_Flow_Sum > 7.50927e+07 )
								if( rsi1 <= 69.5575 )
									ret := 0.634855
								if( rsi1 > 69.5575 )
									ret := 0.160000
						if( rsi1 > 76.2935 )
							if( d_k <= 2.68546 )
								if( Raw_Money_Flow <= 9.56255e+06 )
									ret := -0.742857 // sell
								if( Raw_Money_Flow > 9.56255e+06 )
									ret := 0.323864
							if( d_k > 2.68546 )
								if( smoothD_d <= 84.0987 )
									ret := -0.210526
								if( smoothD_d > 84.0987 )
									ret := -0.733333 // sell
					if( Typical_Price > 132.517 )
						if( Money_Flow_Ratio <= 1.81695 )
							if( Typical_Price <= 134.012 )
								ret := -0.846154 // sell
							if( Typical_Price > 134.012 )
								if( rsi1 <= 55.6136 )
									ret := 0.178082
								if( rsi1 > 55.6136 )
									ret := 0.529412
						if( Money_Flow_Ratio > 1.81695 )
							if( smoothK_k <= 80.9825 )
								if( d_k <= -12.2777 )
									ret := 0.526316
								if( d_k > -12.2777 )
									ret := -0.258182
							if( smoothK_k > 80.9825 )
								if( rsi1 <= 76.0586 )
									ret := 0.387097
								if( rsi1 > 76.0586 )
									ret := -0.188679
				if( Raw_Money_Flow > 4.6458e+07 )
					if( Positive_Money_Flow_Sum <= 2.96523e+08 )
						if( MFI <= 98.1981 )
							if( Positive_Money_Flow_Sum <= 1.46287e+08 )
								ret := -0.040000
							if( Positive_Money_Flow_Sum > 1.46287e+08 )
								if( Money_Flow_Ratio <= 12.15 )
									ret := -0.577273
								if( Money_Flow_Ratio > 12.15 )
									ret := -0.281250
						if( MFI > 98.1981 )
							ret := 0.500000
					if( Positive_Money_Flow_Sum > 2.96523e+08 )
						if( MFI_High <= 7.23724 )
							if( MFI_Low <= 47.6576 )
								if( rsi1 <= 54.6023 )
									ret := 0.444444
								if( rsi1 > 54.6023 )
									ret := -0.545455
							if( MFI_Low > 47.6576 )
								if( smoothK_k <= 88.9968 )
									ret := 0.790698 // buy
								if( smoothK_k > 88.9968 )
									ret := -0.083333
						if( MFI_High > 7.23724 )
							if( MFI_High <= 14.1008 )
								ret := -0.882353 // sell
							if( MFI_High > 14.1008 )
								ret := -0.142857
			if( Positive_Money_Flow_Sum > 3.56015e+08 )
				if( MFI_Low <= 22.0005 )
					if( Positive_Money_Flow_Sum <= 4.13312e+08 )
						if( MFI_High <= -50.2279 )
							ret := -0.090909
						if( MFI_High > -50.2279 )
							ret := -0.842105 // sell
					if( Positive_Money_Flow_Sum > 4.13312e+08 )
						if( Positive_Money_Flow <= 3.29596e+08 )
							if( Negative_Money_Flow_Sum <= 3.12234e+09 )
								if( smoothD_d <= 56.8809 )
									ret := 0.117647
								if( smoothD_d > 56.8809 )
									ret := 0.857143 // buy
							if( Negative_Money_Flow_Sum > 3.12234e+09 )
								if( Raw_Money_Flow <= 2.47218e+08 )
									ret := -0.952381 // sell
								if( Raw_Money_Flow > 2.47218e+08 )
									ret := 1.000000 // buy
						if( Positive_Money_Flow > 3.29596e+08 )
							if( d <= 76.8814 )
								ret := 0.285714
							if( d > 76.8814 )
								ret := -1.000000 // sell
				if( MFI_Low > 22.0005 )
					if( Typical_Price <= 323.108 )
						if( MFI_High <= -11.2521 )
							if( Positive_Money_Flow_Sum <= 2.79558e+09 )
								if( smoothD_d <= 76.8193 )
									ret := -0.056093
								if( smoothD_d > 76.8193 )
									ret := -0.413675
							if( Positive_Money_Flow_Sum > 2.79558e+09 )
								if( Raw_Money_Flow <= 6.83368e+07 )
									ret := 1.000000 // buy
								if( Raw_Money_Flow > 6.83368e+07 )
									ret := 0.466667
						if( MFI_High > -11.2521 )
							if( Negative_Money_Flow_Sum <= 1.03011e+09 )
								if( rsi1 <= 73.2146 )
									ret := 0.140719
								if( rsi1 > 73.2146 )
									ret := -0.084892
							if( Negative_Money_Flow_Sum > 1.03011e+09 )
								if( Negative_Money_Flow <= 1.88513e+08 )
									ret := 0.672566
								if( Negative_Money_Flow > 1.88513e+08 )
									ret := -0.125000
					if( Typical_Price > 323.108 )
						if( smoothD_d <= 92.8303 )
							if( Positive_Money_Flow <= 2.57437e+08 )
								if( MFI_Low <= 36.605 )
									ret := -1.000000 // sell
								if( MFI_Low > 36.605 )
									ret := -0.384615
							if( Positive_Money_Flow > 2.57437e+08 )
								ret := -1.000000 // sell
						if( smoothD_d > 92.8303 )
							ret := 0.200000
	
    ret //return
// Define expected timeframe based on the selected interval: 15Min pine_value: 15   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  15MIN !!"
if (str.tostring(timeframe.period) != "15")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

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


//CODE associated with the technical indicator L_Stochastic_RSI 
//@version=5
//indicator title="Stochastic RSI", shorttitle="Stoch RSI", format=format.price, precision=2, timeframe="", timeframe_gaps=true)
smoothK = input.int(3, "K", minval=1)
smoothD = input.int(3, "D", minval=1)
lengthRSI = input.int(14, "RSI Length", minval=1)
lengthStoch = input.int(14, "Stochastic Length", minval=1)
src = input(close, title="RSI Source")
rsi1 = ta.rsi(src, lengthRSI)
k = ta.sma(ta.stoch(rsi1, rsi1, rsi1, lengthStoch), smoothK)
d = ta.sma(k, smoothD)
plot(k, "K", color=#2962FF)
plot(d, "D", color=#FF6D00)

d_k = d - k
smoothD_d = d - smoothD
smoothK_k = k - smoothK

h0 = hline(80, "Upper Band", color=#787B86)
hline(50, "Middle Band", color=color.new(#787B86, 50))
h1 = hline(20, "Lower Band", color=#787B86)
fill(h0, h1, color=color.rgb(33, 150, 243, 90), title="Background")
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
float op_operation = decision_tree_0_GME_15Min_60738b27(Positive_Money_Flow_Sum, Raw_Money_Flow, MFI_Low, Negative_Money_Flow, Negative_Money_Flow_Sum, Positive_Money_Flow, Money_Flow_Ratio, MFI, MFI_High, Typical_Price, d, d_k, smoothK_k, k, rsi1, smoothD_d)

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



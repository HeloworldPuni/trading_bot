//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: Ultimate_MA_MTF_V2
// ID_model: SNAP_1Min_1ULT_55a2a179 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_SNAP_1Min_1ULT_55a2a179", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_SNAP_1Min_55a2a179(avg2, cr_down2Int, avg, cr_up2Int, ma_downInt, ma_upInt, cr_upInt, cr_downInt)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8,max_features=sqrt, min_samples_leaf=7,random_state=843828734)
	if( ma_downInt <= 0.5 )
		if( cr_upInt <= 0.5 )
			if( cr_downInt <= 0.5 )
				if( avg2 <= 16.457 )
					if( cr_down2Int <= 0.5 )
						if( cr_up2Int <= 0.5 )
							if( avg <= 16.4387 )
								if( avg <= 16.0359 )
									ret := -0.043584
								if( avg > 16.0359 )
									ret := 0.031876
							if( avg > 16.4387 )
								if( avg2 <= 16.4155 )
									ret := 0.484615
								if( avg2 > 16.4155 )
									ret := 0.225610
						if( cr_up2Int > 0.5 )
							if( avg2 <= 14.6859 )
								if( avg <= 14.1689 )
									ret := -0.185255
								if( avg > 14.1689 )
									ret := -0.609756
							if( avg2 > 14.6859 )
								if( avg2 <= 15.2415 )
									ret := 0.589147
								if( avg2 > 15.2415 )
									ret := -0.134259
					if( cr_down2Int > 0.5 )
						if( avg <= 10.8087 )
							if( avg2 <= 8.86906 )
								if( avg <= 8.84833 )
									ret := 0.205882
								if( avg > 8.84833 )
									ret := -0.875000 // sell
							if( avg2 > 8.86906 )
								if( avg2 <= 9.61719 )
									ret := 0.614173
								if( avg2 > 9.61719 )
									ret := 0.299320
						if( avg > 10.8087 )
							if( avg <= 15.9502 )
								if( avg2 <= 15.8463 )
									ret := -0.215259
								if( avg2 > 15.8463 )
									ret := -0.696970
							if( avg > 15.9502 )
								if( avg <= 16.2289 )
									ret := 0.760870 // buy
								if( avg > 16.2289 )
									ret := 0.142857
				if( avg2 > 16.457 )
					if( avg2 <= 16.5225 )
						if( avg2 <= 16.5121 )
							ret := -0.213333
						if( avg2 > 16.5121 )
							if( avg2 <= 16.5198 )
								ret := -0.953846 // sell
							if( avg2 > 16.5198 )
								ret := -0.562500
					if( avg2 > 16.5225 )
						if( avg <= 16.6015 )
							if( avg <= 16.5369 )
								if( avg <= 16.5049 )
									ret := -0.744186 // sell
								if( avg > 16.5049 )
									ret := -0.292683
							if( avg > 16.5369 )
								if( avg <= 16.5693 )
									ret := 0.675439
								if( avg > 16.5693 )
									ret := 0.200000
						if( avg > 16.6015 )
							if( avg <= 16.9769 )
								if( avg2 <= 16.8627 )
									ret := -0.135838
								if( avg2 > 16.8627 )
									ret := -0.537975
							if( avg > 16.9769 )
								if( avg <= 17.0332 )
									ret := 0.569106
								if( avg > 17.0332 )
									ret := -0.193103
			if( cr_downInt > 0.5 )
				if( cr_down2Int <= 0.5 )
					if( avg <= 16.8529 )
						if( avg <= 9.25039 )
							if( avg <= 9.19693 )
								if( avg2 <= 8.52148 )
									ret := 0.600000
								if( avg2 > 8.52148 )
									ret := -0.078261
							if( avg > 9.19693 )
								if( avg2 <= 9.22705 )
									ret := -0.785714 // sell
								if( avg2 > 9.22705 )
									ret := -0.538462
						if( avg > 9.25039 )
							if( avg2 <= 9.25031 )
								ret := 0.941176 // buy
							if( avg2 > 9.25031 )
								if( avg <= 9.3131 )
									ret := 0.705882 // buy
								if( avg > 9.3131 )
									ret := 0.082725
					if( avg > 16.8529 )
						if( avg2 <= 16.989 )
							if( avg <= 16.9087 )
								ret := -0.750000 // sell
							if( avg > 16.9087 )
								ret := -0.437500
						if( avg2 > 16.989 )
							ret := -0.333333
				if( cr_down2Int > 0.5 )
					if( avg <= 8.97982 )
						if( avg2 <= 8.87134 )
							if( avg <= 8.78495 )
								if( avg2 <= 8.56645 )
									ret := 0.600000
								if( avg2 > 8.56645 )
									ret := 0.454545
							if( avg > 8.78495 )
								if( avg2 <= 8.80833 )
									ret := 1.000000 // buy
								if( avg2 > 8.80833 )
									ret := 0.571429
						if( avg2 > 8.87134 )
							if( avg2 <= 8.90281 )
								ret := 1.000000 // buy
							if( avg2 > 8.90281 )
								ret := 0.857143 // buy
					if( avg > 8.97982 )
						if( avg <= 16.6266 )
							if( avg2 <= 9.12245 )
								if( avg2 <= 9.06869 )
									ret := -0.550000
								if( avg2 > 9.06869 )
									ret := -0.300000
							if( avg2 > 9.12245 )
								if( avg <= 9.33629 )
									ret := 0.700000 // buy
								if( avg > 9.33629 )
									ret := 0.137931
						if( avg > 16.6266 )
							if( avg2 <= 16.7404 )
								ret := -0.333333
							if( avg2 > 16.7404 )
								ret := -0.692308
		if( cr_upInt > 0.5 )
			if( avg <= 8.98324 )
				if( avg <= 8.87115 )
					if( avg <= 8.73877 )
						if( avg <= 8.70363 )
							if( avg2 <= 8.43892 )
								if( avg2 <= 8.38914 )
									ret := -0.700000 // sell
								if( avg2 > 8.38914 )
									ret := -1.000000 // sell
							if( avg2 > 8.43892 )
								if( cr_up2Int <= 0.5 )
									ret := -0.193548
								if( cr_up2Int > 0.5 )
									ret := -0.333333
						if( avg > 8.70363 )
							ret := -0.913043 // sell
					if( avg > 8.73877 )
						if( avg <= 8.76703 )
							ret := 0.285714
						if( avg > 8.76703 )
							if( avg2 <= 8.81018 )
								ret := 0.176471
							if( avg2 > 8.81018 )
								ret := -0.208333
				if( avg > 8.87115 )
					if( avg <= 8.94661 )
						if( avg <= 8.90134 )
							if( avg <= 8.8984 )
								ret := -0.846154 // sell
							if( avg > 8.8984 )
								ret := -0.785714 // sell
						if( avg > 8.90134 )
							if( avg2 <= 8.87844 )
								ret := -0.833333 // sell
							if( avg2 > 8.87844 )
								ret := -1.000000 // sell
					if( avg > 8.94661 )
						if( cr_up2Int <= 0.5 )
							if( avg <= 8.96368 )
								ret := -0.727273 // sell
							if( avg > 8.96368 )
								ret := -0.636364
						if( cr_up2Int > 0.5 )
							ret := -1.000000 // sell
			if( avg > 8.98324 )
				if( avg2 <= 15.2475 )
					if( avg2 <= 14.728 )
						if( cr_up2Int <= 0.5 )
							if( avg2 <= 14.0585 )
								if( avg <= 11.4184 )
									ret := -0.114855
								if( avg > 11.4184 )
									ret := -0.490909
							if( avg2 > 14.0585 )
								if( avg <= 14.5605 )
									ret := 0.134328
								if( avg > 14.5605 )
									ret := 0.612903
						if( cr_up2Int > 0.5 )
							if( avg <= 9.28586 )
								if( avg2 <= 9.23118 )
									ret := -0.188679
								if( avg2 > 9.23118 )
									ret := 1.000000 // buy
							if( avg > 9.28586 )
								if( avg2 <= 13.2575 )
									ret := -0.387755
								if( avg2 > 13.2575 )
									ret := -0.030303
					if( avg2 > 14.728 )
						if( avg2 <= 15.0894 )
							if( avg <= 14.8387 )
								ret := -1.000000 // sell
							if( avg > 14.8387 )
								if( avg <= 15.0135 )
									ret := -0.058824
								if( avg > 15.0135 )
									ret := -0.925000 // sell
						if( avg2 > 15.0894 )
							if( cr_up2Int <= 0.5 )
								if( avg <= 15.2523 )
									ret := 0.325581
								if( avg > 15.2523 )
									ret := -0.941176 // sell
							if( cr_up2Int > 0.5 )
								if( avg2 <= 15.1745 )
									ret := -0.033333
								if( avg2 > 15.1745 )
									ret := -0.692308
				if( avg2 > 15.2475 )
					if( avg2 <= 16.3568 )
						if( avg2 <= 16.078 )
							if( avg <= 16.1244 )
								if( avg2 <= 15.5151 )
									ret := 0.214876
								if( avg2 > 15.5151 )
									ret := -0.069832
							if( avg > 16.1244 )
								ret := -1.000000 // sell
						if( avg2 > 16.078 )
							if( avg2 <= 16.1187 )
								ret := 0.409091
							if( avg2 > 16.1187 )
								if( avg <= 16.2584 )
									ret := 0.128205
								if( avg > 16.2584 )
									ret := 0.375000
					if( avg2 > 16.3568 )
						if( cr_up2Int <= 0.5 )
							if( avg2 <= 16.4668 )
								if( avg <= 16.4477 )
									ret := -0.285714
								if( avg > 16.4477 )
									ret := 0.444444
							if( avg2 > 16.4668 )
								if( avg2 <= 16.52 )
									ret := -0.884615 // sell
								if( avg2 > 16.52 )
									ret := -0.228916
						if( cr_up2Int > 0.5 )
							if( avg <= 16.7039 )
								if( avg2 <= 16.5952 )
									ret := -0.928571 // sell
								if( avg2 > 16.5952 )
									ret := -0.545455
							if( avg > 16.7039 )
								ret := 0.733333 // buy
	if( ma_downInt > 0.5 )
		if( cr_upInt <= 0.5 )
			if( avg2 <= 8.62432 )
				if( avg <= 8.60443 )
					if( avg2 <= 8.29574 )
						if( avg <= 8.29524 )
							if( avg <= 8.28685 )
								if( avg2 <= 8.28709 )
									ret := 1.000000 // buy
								if( avg2 > 8.28709 )
									ret := 0.764706 // buy
							if( avg > 8.28685 )
								ret := 0.583333
						if( avg > 8.29524 )
							ret := 1.000000 // buy
					if( avg2 > 8.29574 )
						if( avg2 <= 8.47198 )
							if( cr_down2Int <= 0.5 )
								if( avg2 <= 8.38916 )
									ret := 0.193182
								if( avg2 > 8.38916 )
									ret := -0.233333
							if( cr_down2Int > 0.5 )
								if( cr_downInt <= 0.5 )
									ret := 0.230769
								if( cr_downInt > 0.5 )
									ret := 0.777778 // buy
						if( avg2 > 8.47198 )
							if( avg2 <= 8.51029 )
								ret := 0.649007
							if( avg2 > 8.51029 )
								if( avg2 <= 8.51617 )
									ret := -0.424242
								if( avg2 > 8.51617 )
									ret := 0.162643
				if( avg > 8.60443 )
					if( avg2 <= 8.59443 )
						ret := -0.428571
					if( avg2 > 8.59443 )
						if( avg <= 8.63125 )
							ret := 0.897436 // buy
						if( avg > 8.63125 )
							ret := 0.692308
			if( avg2 > 8.62432 )
				if( cr_down2Int <= 0.5 )
					if( cr_downInt <= 0.5 )
						if( avg2 <= 16.8874 )
							if( avg <= 16.4703 )
								if( avg <= 16.1811 )
									ret := 0.046345
								if( avg > 16.1811 )
									ret := -0.070407
							if( avg > 16.4703 )
								if( avg <= 16.8278 )
									ret := 0.197224
								if( avg > 16.8278 )
									ret := -0.054878
						if( avg2 > 16.8874 )
							if( cr_up2Int <= 0.5 )
								if( avg2 <= 17.2045 )
									ret := -0.218801
								if( avg2 > 17.2045 )
									ret := 0.842105 // buy
							if( cr_up2Int > 0.5 )
								ret := -1.000000 // sell
					if( cr_downInt > 0.5 )
						if( avg <= 16.7298 )
							if( avg <= 9.21009 )
								if( avg <= 8.65484 )
									ret := 0.916667 // buy
								if( avg > 8.65484 )
									ret := 0.225108
							if( avg > 9.21009 )
								if( avg <= 9.38069 )
									ret := -0.500000
								if( avg > 9.38069 )
									ret := 0.029435
						if( avg > 16.7298 )
							if( avg <= 16.8129 )
								if( avg <= 16.7753 )
									ret := 0.640000
								if( avg > 16.7753 )
									ret := 0.888889 // buy
							if( avg > 16.8129 )
								if( avg2 <= 17.0167 )
									ret := 0.000000
								if( avg2 > 17.0167 )
									ret := 0.666667
				if( cr_down2Int > 0.5 )
					if( avg2 <= 14.0899 )
						if( cr_downInt <= 0.5 )
							if( avg <= 8.77247 )
								ret := -0.750000 // sell
							if( avg > 8.77247 )
								if( avg <= 10.6849 )
									ret := 0.341584
								if( avg > 10.6849 )
									ret := 0.048276
						if( cr_downInt > 0.5 )
							if( avg <= 8.77057 )
								ret := -0.450000
							if( avg > 8.77057 )
								if( avg2 <= 8.86492 )
									ret := 0.724138 // buy
								if( avg2 > 8.86492 )
									ret := 0.230986
					if( avg2 > 14.0899 )
						if( avg <= 14.577 )
							if( avg <= 14.4843 )
								ret := -0.423077
							if( avg > 14.4843 )
								ret := -0.846154 // sell
						if( avg > 14.577 )
							if( cr_downInt <= 0.5 )
								if( avg <= 16.3659 )
									ret := 0.123944
								if( avg > 16.3659 )
									ret := -0.328358
							if( cr_downInt > 0.5 )
								if( avg2 <= 15.1638 )
									ret := 0.108108
								if( avg2 > 15.1638 )
									ret := -0.278075
		if( cr_upInt > 0.5 )
			if( avg <= 8.84365 )
				if( avg <= 8.64002 )
					ret := -0.148936
				if( avg > 8.64002 )
					if( avg <= 8.79775 )
						if( cr_up2Int <= 0.5 )
							if( avg2 <= 8.76916 )
								ret := 0.300000
							if( avg2 > 8.76916 )
								if( avg <= 8.77448 )
									ret := 0.636364
								if( avg > 8.77448 )
									ret := 1.000000 // buy
						if( cr_up2Int > 0.5 )
							ret := 0.600000
					if( avg > 8.79775 )
						if( avg2 <= 8.83734 )
							if( cr_up2Int <= 0.5 )
								ret := -0.307692
							if( cr_up2Int > 0.5 )
								ret := 0.200000
						if( avg2 > 8.83734 )
							ret := 0.857143 // buy
			if( avg > 8.84365 )
				if( cr_up2Int <= 0.5 )
					if( avg <= 8.96736 )
						if( avg <= 8.91334 )
							if( avg <= 8.87364 )
								ret := -0.481481
							if( avg > 8.87364 )
								ret := -0.076923
						if( avg > 8.91334 )
							if( avg <= 8.95317 )
								ret := -0.666667
							if( avg > 8.95317 )
								if( avg <= 8.95897 )
									ret := -1.000000 // sell
								if( avg > 8.95897 )
									ret := -0.842105 // sell
					if( avg > 8.96736 )
						if( avg <= 8.98968 )
							ret := 0.880000 // buy
						if( avg > 8.98968 )
							if( avg2 <= 9.01151 )
								ret := -0.900000 // sell
							if( avg2 > 9.01151 )
								if( avg2 <= 14.1129 )
									ret := -0.184713
								if( avg2 > 14.1129 )
									ret := -0.047000
				if( cr_up2Int > 0.5 )
					if( avg2 <= 9.75156 )
						if( avg <= 8.9335 )
							ret := -0.727273 // sell
						if( avg > 8.9335 )
							if( avg <= 9.28594 )
								if( avg <= 9.00438 )
									ret := 0.333333
								if( avg > 9.00438 )
									ret := -0.255319
							if( avg > 9.28594 )
								if( avg <= 9.4448 )
									ret := 0.500000
								if( avg > 9.4448 )
									ret := 0.030303
					if( avg2 > 9.75156 )
						if( avg <= 15.261 )
							if( avg2 <= 11.0353 )
								if( avg <= 10.7608 )
									ret := -0.517241
								if( avg > 10.7608 )
									ret := 0.666667
							if( avg2 > 11.0353 )
								if( avg <= 11.2886 )
									ret := -0.771429 // sell
								if( avg > 11.2886 )
									ret := -0.513274
						if( avg > 15.261 )
							if( avg <= 16.3544 )
								if( avg2 <= 16.0965 )
									ret := 0.188406
								if( avg2 > 16.0965 )
									ret := 0.750000 // buy
							if( avg > 16.3544 )
								if( avg2 <= 16.5998 )
									ret := -0.437500
								if( avg2 > 16.5998 )
									ret := -0.823529 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator Ultimate_MA_MTF_V2 
//@version=5
//indicator title="CM_Ultimate_MA_MTF_V2", shorttitle="CM_Ultimate_MA_MTF_V2", overlay=true)

// Inputs
src = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input.timeframe(title="Use Different Timeframe? Uncheck Box Above", defval="D")
len = input.int(20, title="Moving Average Length - LookBack Period")
factorT3 = input.float(defval=7, title="Tilson T3 Factor - *.10 - so 7 = .7 etc.", minval=0)
atype = input.int(1, minval=1, maxval=8, title="1=SMA, 2=EMA, 3=WMA, 4=HullMA, 5=VWMA, 6=RMA, 7=TEMA, 8=Tilson T3")
spc = input(false, title="Show Price Crossing 1st Mov Avg - Highlight Bar?")
cc = input(true, title="Change Color Based On Direction?")
smoothe = input.int(2, minval=1, maxval=10, title="Color Smoothing - Setting 1 = No Smoothing")
doma2 = input(false, title="Optional 2nd Moving Average")
spc2 = input(false, title="Show Price Crossing 2nd Mov Avg?")
len2 = input.int(50, title="Moving Average Length - Optional 2nd MA")
sfactorT3 = input.float(defval=7, title="Tilson T3 Factor - *.10 - so 7 = .7 etc.", minval=0)
atype2 = input.int(1, minval=1, maxval=8, title="1=SMA, 2=EMA, 3=WMA, 4=HullMA, 5=VWMA, 6=RMA, 7=TEMA, 8=Tilson T3")
cc2 = input(true, title="Change Color Based On Direction 2nd MA?")
warn = input(false, title="***You Can Turn On The Show Dots Parameter Below Without Plotting 2nd MA to See Crosses***")
warn2 = input(false, title="***If Using Cross Feature W/O Plotting 2ndMA - Make Sure 2ndMA Parameters are Set Correctly***")
sd = input(false, title="Show Dots on Cross of Both MA's")

res = useCurrentRes ? timeframe.period : resCustom

// Hull MA definition
hullma = ta.wma(2 * ta.wma(src, len / 2) - ta.wma(src, len), math.round(math.sqrt(len)))

// TEMA definition
ema1 = ta.ema(src, len)
ema2 = ta.ema(ema1, len)
ema3 = ta.ema(ema2, len)
tema = 3 * (ema1 - ema2) + ema3

// Tilson T3 definition
factor = factorT3 * 0.10
gd(src, len, factor) => ta.ema(src, len) * (1 + factor) - ta.ema(ta.ema(src, len), len) * factor
t3(src, len, factor) => gd(gd(gd(src, len, factor), len, factor), len, factor)
tilT3 = t3(src, len, factor)

avg = atype == 1 ? ta.sma(src, len) : atype == 2 ? ta.ema(src, len) : atype == 3 ? ta.wma(src, len) : atype == 4 ? hullma : atype == 5 ? ta.vwma(src, len) : atype == 6 ? ta.rma(src, len) : atype == 7 ? tema : tilT3

// 2nd MA definitions
hullma2 = ta.wma(2 * ta.wma(src, len2 / 2) - ta.wma(src, len2), math.round(math.sqrt(len2)))
sema1 = ta.ema(src, len2)
sema2 = ta.ema(sema1, len2)
sema3 = ta.ema(sema2, len2)
stema = 3 * (sema1 - sema2) + sema3
sfactor = sfactorT3 * 0.10
sgd(src, len2, sfactor) => ta.ema(src, len2) * (1 + sfactor) - ta.ema(ta.ema(src, len2), len2) * sfactor
st3(src, len2, sfactor) => sgd(sgd(gd(src, len2, sfactor), len2, sfactor), len2, sfactor)
stilT3 = st3(src, len2, sfactor)

avg2 = atype2 == 1 ? ta.sma(src, len2) : atype2 == 2 ? ta.ema(src, len2) : atype2 == 3 ? ta.wma(src, len2) : atype2 == 4 ? hullma2 : atype2 == 5 ? ta.vwma(src, len2) : atype2 == 6 ? ta.rma(src, len2) : atype2 == 7 ? stema : stilT3

out1 = request.security(syminfo.tickerid, res, avg)
out2 = request.security(syminfo.tickerid, res, avg2)

// Formula for Price Crossing Moving Average #1
cr_up = open < out1 and close > out1
cr_down = open > out1 and close < out1

// Formula for Price Crossing Moving Average #2
cr_up2 = open < out2 and close > out2
cr_down2 = open > out2 and close < out2

// Barcolor Criteria for Price Crossing Moving Average #1
iscrossUp() => cr_up
iscrossDown() => cr_down

// Barcolor Criteria for Price Crossing Moving Average #2
iscrossUp2() => cr_up2
iscrossDown2() => cr_down2

ma_up = out1 >= ta.valuewhen(out1[smoothe] >= out1[1], out1[smoothe], 1)
ma_down = out1 < ta.valuewhen(out1[smoothe] < out1[1], out1[smoothe], 1)

col = cc ? (ma_up ? color.lime : ma_down ? color.red : color.aqua) : color.aqua
col2 = cc2 ? (ma_up ? color.lime : ma_down ? color.red : color.aqua) : color.white

plot(out1, title="Multi-Timeframe Moving Avg", linewidth=4, color=col)
plot(doma2 and out2 ? out2 : na, title="2nd Multi-TimeFrame Moving Average", linewidth=4, color=col2)
plot(sd and ta.crossover(out1, out2) ? out2 : na, style=plot.style_cross, linewidth=15, color=color.aqua)

// Barcolor Plot for Price Crossing Moving Average #1
barcolor(spc and iscrossUp() ? color.yellow : na)
barcolor(spc and iscrossDown() ? color.yellow : na)

// Barcolor Plot for Price Crossing Moving Average #2
barcolor(spc2 and iscrossUp2() ? color.yellow : na)
barcolor(spc2 and iscrossDown2() ? color.yellow : na)

cr_upInt = cr_up ? 1: 0    //Bool to int
cr_up2Int = cr_up2 ? 1: 0    //Bool to int
cr_downInt = cr_down ? 1: 0    //Bool to int
cr_down2Int = cr_down2 ? 1: 0    //Bool to int
ma_upInt = ma_up ? 1: 0    //Bool to int
ma_downInt = ma_down ? 1: 0    //Bool to int

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
float op_operation = decision_tree_0_SNAP_1Min_55a2a179(avg2, cr_down2Int, avg, cr_up2Int, ma_downInt, ma_upInt, cr_upInt, cr_downInt)

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



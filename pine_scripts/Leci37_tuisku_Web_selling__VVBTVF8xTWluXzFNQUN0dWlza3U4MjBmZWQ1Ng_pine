//Welcome to © Tuisku Trading Strategy, a sophisticated and optimised solution created by the experienced team at Tuisku.eu. Our team of experts specialise in random forest AI, harnessing its powerful capabilities to improve trading performance.
//Tuisku's commitment to quality and innovation shines through in every aspect of this strategy.


// Technical base pattern: MACD_ULT_MTF
// ID_model: UPST_1Min_1MAC_820fed56 Date Creation: 2024/10/18 Recommended expiry date : 2025/06/18
//@version=5
strategy("Tuisku_UPST_1Min_1MAC_820fed56", overlay=true, margin_long=1000, margin_short=1000, pyramiding=1)
//RANDOM FOREST AI 
decision_tree_0_UPST_1Min_820fed56(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)=>
	var float ret = 0  // # DecisionTreeRegressor(criterion=friedman_mse, max_depth=8, max_features=0.7,min_samples_leaf=4, min_samples_split=5,random_state=843828734)
	if( histA_IsUpInt <= 0.5 )
		if( histB_IsDownInt <= 0.5 )
			if( macd <= 0.185128 )
				if( macd <= -0.347188 )
					if( hist <= -0.092744 )
						if( macd <= -1.18946 )
							ret := 0.500000
						if( macd > -1.18946 )
							if( hist <= -0.241809 )
								ret := 0.750000 // buy
							if( hist > -0.241809 )
								if( hist <= -0.119198 )
									ret := 1.000000 // buy
								if( hist > -0.119198 )
									ret := 0.900000 // buy
					if( hist > -0.092744 )
						if( macd <= -0.408632 )
							if( signal <= -0.50153 )
								ret := 1.000000 // buy
							if( signal > -0.50153 )
								if( hist <= -0.040317 )
									ret := -0.500000
								if( hist > -0.040317 )
									ret := -1.000000 // sell
						if( macd > -0.408632 )
							if( signal <= -0.32894 )
								if( macd <= -0.365648 )
									ret := 0.666667
								if( macd > -0.365648 )
									ret := 0.166667
							if( signal > -0.32894 )
								if( macd <= -0.35368 )
									ret := 0.615385
								if( macd > -0.35368 )
									ret := 1.000000 // buy
				if( macd > -0.347188 )
					if( signal <= 0.037398 )
						if( hist <= 0.019685 )
							if( signal <= -0.122693 )
								if( signal <= -0.147447 )
									ret := 0.034664
								if( signal > -0.147447 )
									ret := -0.190291
							if( signal > -0.122693 )
								if( macd <= -0.150951 )
									ret := -0.398936
								if( macd > -0.150951 )
									ret := 0.043794
						if( hist > 0.019685 )
							if( macd <= -0.040956 )
								if( macd <= -0.155372 )
									ret := 0.056962
								if( macd > -0.155372 )
									ret := 0.376704
							if( macd > -0.040956 )
								if( signal <= -0.065743 )
									ret := -0.322870
								if( signal > -0.065743 )
									ret := 0.091803
					if( signal > 0.037398 )
						if( macd_IsBelowInt <= 0.5 )
							if( hist <= 0.038623 )
								if( hist <= 0.021097 )
									ret := -0.039700
								if( hist > 0.021097 )
									ret := -0.150549
							if( hist > 0.038623 )
								if( signal <= 0.124718 )
									ret := 0.245066
								if( signal > 0.124718 )
									ret := -0.227273
						if( macd_IsBelowInt > 0.5 )
							if( macd <= -0.007431 )
								if( hist <= -0.144686 )
									ret := -0.142857
								if( hist > -0.144686 )
									ret := 0.627660
							if( macd > -0.007431 )
								if( macd <= 0.161369 )
									ret := -0.027981
								if( macd > 0.161369 )
									ret := -0.500000
			if( macd > 0.185128 )
				if( hist <= 0.176134 )
					if( hist <= -0.073872 )
						if( signal <= 0.362051 )
							ret := -1.000000 // sell
						if( signal > 0.362051 )
							if( macd <= 0.663941 )
								if( hist <= -0.084371 )
									ret := 0.750000 // buy
								if( hist > -0.084371 )
									ret := -0.250000
							if( macd > 0.663941 )
								ret := -0.800000 // sell
					if( hist > -0.073872 )
						if( macd <= 0.232356 )
							if( macd <= 0.215252 )
								if( signal <= 0.192621 )
									ret := 0.064935
								if( signal > 0.192621 )
									ret := 0.639456
							if( macd > 0.215252 )
								if( signal <= 0.216385 )
									ret := 0.742424 // buy
								if( signal > 0.216385 )
									ret := 0.389831
						if( macd > 0.232356 )
							if( signal <= 0.38093 )
								if( signal <= 0.159234 )
									ret := 0.578947
								if( signal > 0.159234 )
									ret := 0.001511
							if( signal > 0.38093 )
								if( signal <= 0.574489 )
									ret := 0.689076
								if( signal > 0.574489 )
									ret := -0.500000
				if( hist > 0.176134 )
					if( signal <= 0.359544 )
						if( signal <= 0.103479 )
							ret := -0.833333 // sell
						if( signal > 0.103479 )
							ret := 0.250000
					if( signal > 0.359544 )
						ret := -1.000000 // sell
		if( histB_IsDownInt > 0.5 )
			if( signal <= -0.227897 )
				if( hist <= -0.012208 )
					if( macd <= -0.617533 )
						ret := 0.000000
					if( macd > -0.617533 )
						if( hist <= -0.025485 )
							if( hist <= -0.046009 )
								if( macd <= -0.312226 )
									ret := 0.750000 // buy
								if( macd > -0.312226 )
									ret := 0.950000 // buy
							if( hist > -0.046009 )
								if( hist <= -0.040295 )
									ret := -0.600000
								if( hist > -0.040295 )
									ret := 0.529412
						if( hist > -0.025485 )
							if( hist <= -0.018694 )
								if( macd <= -0.260702 )
									ret := 1.000000 // buy
								if( macd > -0.260702 )
									ret := 0.833333 // buy
							if( hist > -0.018694 )
								if( hist <= -0.013881 )
									ret := 0.666667
								if( hist > -0.013881 )
									ret := 1.000000 // buy
				if( hist > -0.012208 )
					if( signal <= -0.295565 )
						if( signal <= -0.322791 )
							ret := 0.400000
						if( signal > -0.322791 )
							ret := 1.000000 // buy
					if( signal > -0.295565 )
						if( macd <= -0.247565 )
							ret := -1.000000 // sell
						if( macd > -0.247565 )
							if( signal <= -0.230736 )
								ret := -0.250000
							if( signal > -0.230736 )
								ret := 0.000000
			if( signal > -0.227897 )
				if( hist <= -0.121788 )
					if( macd <= -0.289318 )
						if( macd <= -0.345971 )
							if( signal <= -0.129685 )
								ret := -1.000000 // sell
							if( signal > -0.129685 )
								ret := -0.500000
						if( macd > -0.345971 )
							if( hist <= -0.141616 )
								ret := -0.800000 // sell
							if( hist > -0.141616 )
								ret := 0.000000
					if( macd > -0.289318 )
						if( macd <= 0.355001 )
							if( signal <= 0.372157 )
								if( hist <= -0.160072 )
									ret := 0.818182 // buy
								if( hist > -0.160072 )
									ret := 0.402299
							if( signal > 0.372157 )
								ret := -0.714286 // sell
						if( macd > 0.355001 )
							ret := 1.000000 // buy
				if( hist > -0.121788 )
					if( macd <= -0.090611 )
						if( hist <= -0.006035 )
							if( macd <= -0.270703 )
								if( signal <= -0.206701 )
									ret := 0.666667
								if( signal > -0.206701 )
									ret := -0.285714
							if( macd > -0.270703 )
								if( hist <= -0.062675 )
									ret := -0.153348
								if( hist > -0.062675 )
									ret := -0.011905
						if( hist > -0.006035 )
							if( macd <= -0.207627 )
								ret := -1.000000 // sell
							if( macd > -0.207627 )
								if( signal <= -0.147136 )
									ret := 0.888889 // buy
								if( signal > -0.147136 )
									ret := 0.295455
					if( macd > -0.090611 )
						if( signal <= -0.054377 )
							if( signal <= -0.080184 )
								if( signal <= -0.080563 )
									ret := -0.238095
								if( signal > -0.080563 )
									ret := -1.000000 // sell
							if( signal > -0.080184 )
								if( macd <= -0.0653 )
									ret := 0.300000
								if( macd > -0.0653 )
									ret := 0.662338
						if( signal > -0.054377 )
							if( hist <= -0.085089 )
								if( macd <= 0.068675 )
									ret := 0.119318
								if( macd > 0.068675 )
									ret := -0.425532
							if( hist > -0.085089 )
								if( signal <= 0.39631 )
									ret := 0.118142
								if( signal > 0.39631 )
									ret := -0.366197
	if( histA_IsUpInt > 0.5 )
		if( signal <= -0.060643 )
			if( hist <= 0.065225 )
				if( macd <= -0.298658 )
					if( macd <= -0.339269 )
						if( hist <= 0.022325 )
							ret := -0.250000
						if( hist > 0.022325 )
							if( signal <= -0.457468 )
								ret := 0.500000
							if( signal > -0.457468 )
								ret := 1.000000 // buy
					if( macd > -0.339269 )
						if( macd <= -0.305895 )
							if( hist <= 0.031724 )
								if( macd <= -0.323663 )
									ret := -0.875000 // sell
								if( macd > -0.323663 )
									ret := -1.000000 // sell
							if( hist > 0.031724 )
								ret := -0.500000
						if( macd > -0.305895 )
							if( hist <= 0.025935 )
								if( macd <= -0.300969 )
									ret := -0.500000
								if( macd > -0.300969 )
									ret := -1.000000 // sell
							if( hist > 0.025935 )
								ret := 0.000000
				if( macd > -0.298658 )
					if( hist <= 0.049016 )
						if( macd <= -0.03275 )
							if( macd <= -0.26503 )
								if( macd <= -0.291372 )
									ret := 0.200000
								if( macd > -0.291372 )
									ret := 0.750000 // buy
							if( macd > -0.26503 )
								if( hist <= 0.00068 )
									ret := 0.416667
								if( hist > 0.00068 )
									ret := 0.059814
						if( macd > -0.03275 )
							if( macd <= -0.022648 )
								if( macd <= -0.029169 )
									ret := 0.733333 // buy
								if( macd > -0.029169 )
									ret := 0.156250
							if( macd > -0.022648 )
								if( signal <= -0.063894 )
									ret := 0.947368 // buy
								if( signal > -0.063894 )
									ret := 0.823529 // buy
					if( hist > 0.049016 )
						if( macd <= -0.108316 )
							if( hist <= 0.059133 )
								if( macd <= -0.249073 )
									ret := 0.125000
								if( macd > -0.249073 )
									ret := -0.494118
							if( hist > 0.059133 )
								if( hist <= 0.059899 )
									ret := 0.333333
								if( hist > 0.059899 )
									ret := -0.142857
						if( macd > -0.108316 )
							if( macd <= -0.098809 )
								if( hist <= 0.059964 )
									ret := 0.241379
								if( hist > 0.059964 )
									ret := 1.000000 // buy
							if( macd > -0.098809 )
								if( signal <= -0.094332 )
									ret := -0.240602
								if( signal > -0.094332 )
									ret := 0.083333
			if( hist > 0.065225 )
				if( macd <= -0.078584 )
					if( signal <= -0.20376 )
						if( hist <= 0.098956 )
							if( signal <= -0.209897 )
								if( macd <= -0.149987 )
									ret := 0.192982
								if( macd > -0.149987 )
									ret := -0.466667
							if( signal > -0.209897 )
								if( signal <= -0.205487 )
									ret := 0.777778 // buy
								if( signal > -0.205487 )
									ret := -0.500000
						if( hist > 0.098956 )
							if( macd <= -0.224791 )
								if( macd <= -0.68414 )
									ret := 0.500000
								if( macd > -0.68414 )
									ret := 0.968750 // buy
							if( macd > -0.224791 )
								if( hist <= 0.114195 )
									ret := 1.000000 // buy
								if( hist > 0.114195 )
									ret := 0.357143
					if( signal > -0.20376 )
						if( macd <= -0.108798 )
							if( hist <= 0.067904 )
								ret := 0.750000 // buy
							if( hist > 0.067904 )
								if( hist <= 0.075945 )
									ret := 1.000000 // buy
								if( hist > 0.075945 )
									ret := 0.833333 // buy
						if( macd > -0.108798 )
							if( macd <= -0.086743 )
								if( signal <= -0.176635 )
									ret := 0.888889 // buy
								if( signal > -0.176635 )
									ret := 0.352941
							if( macd > -0.086743 )
								if( macd <= -0.080049 )
									ret := 0.958333 // buy
								if( macd > -0.080049 )
									ret := 0.600000
				if( macd > -0.078584 )
					if( hist <= 0.072547 )
						if( hist <= 0.066924 )
							if( macd <= -0.035839 )
								if( hist <= 0.066268 )
									ret := 0.750000 // buy
								if( hist > 0.066268 )
									ret := 1.000000 // buy
							if( macd > -0.035839 )
								if( signal <= -0.076959 )
									ret := -0.333333
								if( signal > -0.076959 )
									ret := 1.000000 // buy
						if( hist > 0.066924 )
							if( macd <= -0.075939 )
								ret := -1.000000 // sell
							if( macd > -0.075939 )
								if( macd <= -0.058555 )
									ret := 0.863636 // buy
								if( macd > -0.058555 )
									ret := 0.150943
					if( hist > 0.072547 )
						if( hist <= 0.088713 )
							if( signal <= -0.124253 )
								if( macd <= -0.066088 )
									ret := -1.000000 // sell
								if( macd > -0.066088 )
									ret := -0.421053
							if( signal > -0.124253 )
								if( hist <= 0.075082 )
									ret := 0.333333
								if( hist > 0.075082 )
									ret := -0.288462
						if( hist > 0.088713 )
							if( hist <= 0.125043 )
								if( macd <= -0.035698 )
									ret := 0.074074
								if( macd > -0.035698 )
									ret := 0.638889
							if( hist > 0.125043 )
								if( hist <= 0.174042 )
									ret := -0.666667
								if( hist > 0.174042 )
									ret := 0.000000
		if( signal > -0.060643 )
			if( signal <= 0.097058 )
				if( hist <= 0.011241 )
					if( macd <= 0.097491 )
						if( macd <= 0.078518 )
							if( macd <= 0.066345 )
								if( macd <= 0.065059 )
									ret := 0.022936
								if( macd > 0.065059 )
									ret := 0.666667
							if( macd > 0.066345 )
								if( macd <= 0.076388 )
									ret := -0.298701
								if( macd > 0.076388 )
									ret := -0.580645
						if( macd > 0.078518 )
							if( macd <= 0.082391 )
								if( hist <= 0.002249 )
									ret := 0.222222
								if( hist > 0.002249 )
									ret := 0.682927
							if( macd > 0.082391 )
								if( signal <= 0.074401 )
									ret := -1.000000 // sell
								if( signal > 0.074401 )
									ret := 0.128713
					if( macd > 0.097491 )
						if( macd <= 0.099251 )
							ret := -1.000000 // sell
						if( macd > 0.099251 )
							if( hist <= 0.009113 )
								ret := 0.000000
							if( hist > 0.009113 )
								ret := -1.000000 // sell
				if( hist > 0.011241 )
					if( macd <= 0.104217 )
						if( macd <= 0.102779 )
							if( signal <= -0.013888 )
								if( macd <= -0.007572 )
									ret := -0.057295
								if( macd > -0.007572 )
									ret := -0.216160
							if( signal > -0.013888 )
								if( signal <= 0.01663 )
									ret := -0.000817
								if( signal > 0.01663 )
									ret := -0.115517
						if( macd > 0.102779 )
							if( signal <= 0.072439 )
								if( macd <= 0.103809 )
									ret := 0.882353 // buy
								if( macd > 0.103809 )
									ret := 0.375000
							if( signal > 0.072439 )
								if( signal <= 0.079324 )
									ret := -0.400000
								if( signal > 0.079324 )
									ret := 0.750000 // buy
					if( macd > 0.104217 )
						if( hist <= 0.034257 )
							if( hist <= 0.016988 )
								if( hist <= 0.016499 )
									ret := -0.600000
								if( hist > 0.016499 )
									ret := 0.250000
							if( hist > 0.016988 )
								if( macd <= 0.105921 )
									ret := -0.363636
								if( macd > 0.105921 )
									ret := -0.741573 // sell
						if( hist > 0.034257 )
							if( signal <= 0.067365 )
								if( macd <= 0.179784 )
									ret := -0.333333
								if( macd > 0.179784 )
									ret := -1.000000 // sell
							if( signal > 0.067365 )
								if( macd <= 0.119847 )
									ret := -0.383333
								if( macd > 0.119847 )
									ret := 0.196319
			if( signal > 0.097058 )
				if( signal <= 0.200027 )
					if( hist <= 0.006146 )
						if( macd <= 0.105158 )
							if( hist <= 0.004361 )
								if( hist <= 0.003483 )
									ret := 0.714286 // buy
								if( hist > 0.003483 )
									ret := -0.250000
							if( hist > 0.004361 )
								ret := 1.000000 // buy
						if( macd > 0.105158 )
							if( macd <= 0.112943 )
								if( signal <= 0.108952 )
									ret := -0.062500
								if( signal > 0.108952 )
									ret := -0.960000 // sell
							if( macd > 0.112943 )
								if( macd <= 0.119008 )
									ret := 0.578947
								if( macd > 0.119008 )
									ret := -0.230769
					if( hist > 0.006146 )
						if( macd <= 0.114102 )
							if( macd <= 0.107418 )
								if( signal <= 0.098552 )
									ret := 1.000000 // buy
								if( signal > 0.098552 )
									ret := 0.333333
							if( macd > 0.107418 )
								if( hist <= 0.009206 )
									ret := 0.937500 // buy
								if( hist > 0.009206 )
									ret := 0.714286 // buy
						if( macd > 0.114102 )
							if( macd <= 0.11961 )
								if( signal <= 0.106165 )
									ret := -0.166667
								if( signal > 0.106165 )
									ret := -1.000000 // sell
							if( macd > 0.11961 )
								if( signal <= 0.118021 )
									ret := 0.114391
								if( signal > 0.118021 )
									ret := 0.334579
				if( signal > 0.200027 )
					if( macd <= 0.412669 )
						if( hist <= 0.034599 )
							if( signal <= 0.223592 )
								if( hist <= 0.015593 )
									ret := -0.025641
								if( hist > 0.015593 )
									ret := -0.833333 // sell
							if( signal > 0.223592 )
								if( signal <= 0.353098 )
									ret := 0.593023
								if( signal > 0.353098 )
									ret := -0.700000 // sell
						if( hist > 0.034599 )
							if( hist <= 0.053626 )
								if( macd <= 0.381091 )
									ret := -0.809524 // sell
								if( macd > 0.381091 )
									ret := 0.000000
							if( hist > 0.053626 )
								if( macd <= 0.349882 )
									ret := 0.166667
								if( macd > 0.349882 )
									ret := -0.740741 // sell
					if( macd > 0.412669 )
						if( signal <= 0.447912 )
							if( macd <= 0.513068 )
								if( macd <= 0.440875 )
									ret := 0.470588
								if( macd > 0.440875 )
									ret := 1.000000 // buy
							if( macd > 0.513068 )
								ret := -0.500000
						if( signal > 0.447912 )
							if( macd <= 0.569684 )
								ret := -0.500000
							if( macd > 0.569684 )
								ret := -1.000000 // sell
	
    ret //return
// Define expected timeframe based on the selected interval: 1Min pine_value: 1   Trigger an alert and show a label if the timeframe is incorrect
alert_message_time_wrong = "The current candle TIMEframe is WRONG: "+ str.tostring(timeframe.period) + ", CHANGE it to the CORRECT one:  1MIN !!"
if (str.tostring(timeframe.period) != "1")
    alert(alert_message_time_wrong, alert.freq_once_per_bar_close)
    label.new(bar_index -300, high+30, text = alert_message_time_wrong, style = label.style_label_down,size = size.large, color = color.red, textcolor = color.white)
    log.error(alert_message_time_wrong)

//CODE associated with the technical indicator MACD_ULT_MTF 
//@version=5
//indicator title="CM_MacD_Ult_MTF", shorttitle="CM_Ult_MacD_MTF", overlay=false)

source = close
useCurrentRes = input(true, title="Use Current Chart Resolution?")
resCustom = input.timeframe(title="Use Different Timeframe? Uncheck Box Above", defval="60")
smd = input(true, title="Show MacD & Signal Line? Also Turn Off Dots Below")
sd = input(true, title="Show Dots When MacD Crosses Signal Line?")
sh = input(true, title="Show Histogram?")
macd_colorChange = input(true,title="Change MacD Line Color-Signal Line Cross?")
hist_colorChange = input(true,title="MacD Histogram 4 Colors?")

res = useCurrentRes ? timeframe.period : resCustom

fastLength = input.int(12, minval=1)
slowLength = input.int(26, minval=1)
signalLength = input.int(9, minval=1)

fastMA = ta.ema(source, fastLength)
slowMA = ta.ema(source, slowLength)

macd = fastMA - slowMA
signal = ta.sma(macd, signalLength)
hist = macd - signal

outMacD = request.security(syminfo.tickerid, res, macd)
outSignal = request.security(syminfo.tickerid, res, signal)
outHist = request.security(syminfo.tickerid, res, hist)

histA_IsUp = outHist > outHist[1] and outHist > 0
histA_IsDown = outHist < outHist[1] and outHist > 0
histB_IsDown = outHist < outHist[1] and outHist <= 0
histB_IsUp = outHist > outHist[1] and outHist <= 0

// MacD Color Definitions
macd_IsAbove = outMacD >= outSignal
macd_IsBelow = outMacD < outSignal

plot_color = hist_colorChange ? histA_IsUp ? color.aqua : histA_IsDown ? color.blue : histB_IsDown ? color.red : histB_IsUp ? color.maroon : color.yellow : color.gray
macd_color = macd_colorChange ? macd_IsAbove ? color.lime : color.red : color.red
signal_color = macd_colorChange ? macd_IsAbove ? color.yellow : color.yellow : color.lime

circleYPosition = outSignal

plot(smd and outMacD ? outMacD : na, title="MACD", color=macd_color, linewidth=4)
plot(smd and outSignal ? outSignal : na, title="Signal Line", color=signal_color, style=plot.style_line, linewidth=2)
plot(sh and outHist ? outHist : na, title="Histogram", color=plot_color, style=plot.style_histogram, linewidth=4)
plot(sd and ta.cross(outMacD, outSignal) ? circleYPosition : na, title="Cross", style=plot.style_circles, linewidth=4, color=macd_color)
hline(0, '0 Line', linestyle=hline.style_solid, linewidth=2, color=color.white)

histA_IsUpInt = histA_IsUp ? 1: 0
histA_IsDownInt = histA_IsDown ? 1: 0
histB_IsDownInt = histB_IsDown ? 1: 0
histB_IsUpInt = histB_IsUp ? 1: 0
macd_IsAboveInt = macd_IsAbove ? 1: 0
macd_IsBelowInt = macd_IsBelow ? 1: 0

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
float op_operation = decision_tree_0_UPST_1Min_820fed56(histB_IsUpInt, macd_IsBelowInt, macd, histB_IsDownInt, macd_IsAboveInt, histA_IsDownInt, histA_IsUpInt, hist, signal)

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



import quandl
from finquant.portfolio import build_portfolio
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')
start_date = '2015-01-01'
end_date = '2017-12-31'

names = ['GOOG','FB', 'AAPL', 'AMZN', 'DIS']

# names = ['GOOG', 'AMZN', "FB", 'AAPL']

pf = build_portfolio(names=names,
                    start_date=start_date,
                    end_date=end_date,
                     data_api = 'yfinance')

print(pf.data.head())


# PortFolio Propeties
print(pf.properties())

# Cumulative Returns
pf.comp_cumulative_returns().plot().axhline(y=0,
                                            color ='black',
                                            lw =3)
# Band Moving Average (Buy/sell Signala)
from finquant.moving_average import compute_ma, ema
dis = pf.get_stock("DIS").data.copy(deep=True)
spans = [10,50,100,150,200]
ma = compute_ma(dis, ema, spans=spans,
                plot=True)

# Bolinger Bands
from finquant.moving_average import plot_bollinger_band
dis = pf.get_stock("DIS").data.copy(deep = True)
span = 20
# plot_bollinger_band(dis, sma, span)


# PortFolio Optimization
opt_w, opt_res = pf.mc_optimisation(num_trials=5000)
pf.mc_plot_results()
pf.ef_plot_efrontier()
pf.ef_plot_optimal_portfolios()
pf.plot_stocks()
plt.show()



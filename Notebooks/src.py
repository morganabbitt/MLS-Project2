import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import ast
plt.style.use('ggplot')


def plotting_player_location_frame(frame_number:int):
    
    df_final = pd.read_csv('../data/SecondSpectrum_Data.csv', index_col=0)
    
    lst_home_start = ast.literal_eval(df_final['homePlayers'][frame_number])
    lst_away_start = ast.literal_eval(df_final['awayPlayers'][frame_number])
    
    array = np.empty((11, 3))
    array2 = np.empty((11, 3))


    for i, (player_home, player_away) in enumerate(zip(lst_home_start, lst_away_start)):
        array[i][0] = player_home['xyz'][0]
        array[i][1] = player_home['xyz'][1]
        array[i][2] = player_home['xyz'][2]

        array2[i][0] = player_away['xyz'][0]
        array2[i][1] = player_away['xyz'][1]
        array2[i][2] = player_away['xyz'][2]
    print('Player Locs: {}'.format(array))
    
    ball_x, ball_y, ball_z = ast.literal_eval(df_final['ball.xyz'][frame_number])
    ball_posession = df_final['lastTouch'][frame_number]
    if ball_posession == 'away':
        color_ = 'navy'
    else:
        color_ = 'forestgreen'
    
    fig, ax = plt.subplots(figsize=(19, 18))
    
    img = plt.imread('../printable-soccer-field-diagram.png')
    ax.imshow(img, extent=(-51.44, 51.44, -34.29, 34.29))
    plt.scatter(array[:, 0], array[:, 1], s=150, label='Portland Timbers', color='forestgreen')
    plt.scatter(array2[:, 0],  array2[:, 1], s=150, label='Nashville SC', color='navy')
    plt.scatter(ball_x, ball_y, marker='*', s=350, color=color_, edgecolors='black', linewidths=1)
    plt.xticks([])
    plt.yticks([])
    plt.legend(loc='upper center', fontsize='large')
    plt.show()
    print('Time of Frame: {:2.2f} minutes'.format(df_final['gameClock'][frame_number] / 25))
    
def plot_field():
    
    fig, ax1 = plt.subplots(figsize=(19, 18))  
    img = plt.imread('../printable-soccer-field-diagram.png')
    ax1.imshow(img, extent=(-51.44, 51.44, -34.29, 34.29))
    
    plt.xticks([])
    plt.yticks([])
    plt.show()

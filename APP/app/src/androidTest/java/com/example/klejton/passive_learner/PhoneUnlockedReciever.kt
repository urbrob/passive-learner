package com.example.klejton.passive_learner

import android.app.KeyguardManager
import android.content.Intent
import android.content.BroadcastReceiver
import android.content.Context


class PhoneUnlockedReceiver : BroadcastReceiver()
{
    override fun onReceive(context: Context, intent: Intent)
    {
        val keyguardManager = context.getSystemService(Context.KEYGUARD_SERVICE) as KeyguardManager
        if (keyguardManager.isKeyguardSecure)
        {

            //phone was unlocked, do stuff here

        }
    }
}
package passive_learner.urbrob.github.com.app

import android.content.Context

class FileManager(context: MainActivity) {
    val ctx: MainActivity = context

    fun saveFileToLocalResources(fileName: String, content: String) {
        ctx.openFileOutput(fileName, Context.MODE_PRIVATE).use {
            it.write(content.toByteArray())
        }
    }

}